import logging
import time
from typing import Any, cast

import requests

logger = logging.getLogger("HeadHunterApi")


class HeadHunterApi:
    """Класс для работы с API сайта HeadHunter, получения списков вакансий и работодателей.

    Attributes:
        _search_text (str): Текст поиска в названиях вакансий
        _search_area (str): Регион поиска
    """

    BASE_URL = "https://api.hh.ru"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Connection": "keep-alive",
    }

    def __init__(self, search_text: str, search_area: str) -> None:
        self._search_text = search_text
        self._search_area = search_area

    @staticmethod
    def _make_request(
        url: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
    ) -> Any:
        """
        Выполняет GET-запрос к указанному URL с параметрами и заголовками.
        Проверяет статус ответа и возвращает декодированный JSON.
        В случае ошибки пытается подключиться еще 2 раза, затем выбрасывает исключение.
        """
        for attempt in range(3):
            response = requests.get(url, params=params, headers=headers)

            if response.status_code == 200:
                logger.info("Успешное подключение.")
                return cast(dict[str, Any], response.json())
            elif response.status_code != 200:
                logger.warning(
                    f"Ошибка подключения к ресурсу: {response.status_code}. Попытка повторного подключения."
                )
                time.sleep(2)

        info = f"Ошибка подключения: {response.status_code} - {response.text}"
        logger.error(info)
        raise ConnectionError(info)

    def get_employers_vacancies(self, employer_id: str) -> list[dict | None]:
        """Метод получения информации об открытых вакансиях работодателя.

        Args:
            employer_id (str): Уникальный идентификационный номер работодателя на HH.ru
        """
        url = f"{self.BASE_URL}/vacancies"
        params = {
            "employer_id": employer_id,
            "text": self._search_text,
            "area": self._search_area,
            "per_page": 20,
            "page": 1,
        }
        data = self._make_request(url, params=params, headers=self.HEADERS)
        vacancies_list = []

        if len(data["items"]) > 0:
            vacancies_list.extend(data["items"])

            if data["pages"] > 2:
                params = {
                    "employer_id": employer_id,
                    "text": self._search_text,
                    "area": self._search_area,
                    "per_page": 20,
                    "page": 2,
                }

                time.sleep(2)
                data = self._make_request(url, params=params, headers=self.HEADERS)

                vacancies_list.extend(data["items"])

        return vacancies_list

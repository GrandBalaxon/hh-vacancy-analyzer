from typing import Any, cast

import requests


class HeadHunterApi:
    """Класс для работы с API сайта HeadHunter, получения списков вакансий и работодателей."""

    BASE_URL = "https://api.hh.ru"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Connection": "keep-alive"
    }

    def __init__(self, company_name: str, search_text: str, search_area: str) -> None:
        self._company_name = company_name
        self._search_text = search_text
        self._search_area = search_area
        self._company_employers_ids = []

    @staticmethod
    def _make_request(
        url: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
    ) -> Any:
        """
        Выполняет GET-запрос к указанному URL с параметрами и заголовками.
        Проверяет статус ответа и возвращает декодированный JSON.
        В случае ошибки выбрасывает исключение.
        """
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Ошибка подключения: {response.status_code} - {response.text}")

        return cast(dict[str, Any], response.json())

    def get_employers_vacancies(self, employer_id: str) -> list[dict | None]:
        """"""
        url = f"{self.BASE_URL}/vacancies"
        params = {
            "employer_id": employer_id,
            "text": self._search_text,
            "area": self._search_area,
            "per_page": 100,
        }
        data = self._make_request(url, params=params, headers=self.HEADERS)
        vacancies_list = []

        if len(data["items"]) > 0:
            pages = data["pages"]

            for page_num in range(pages):
                params = {
                    "employer_id": employer_id,
                    "text": self._search_text,
                    "area": self._search_area,
                    "per_page": 100,
                    "page": page_num,
                }
                data = self._make_request(url, params=params, headers=self.HEADERS)

                vacancies_list.extend(data["items"])

        return vacancies_list

    def get_company_employers_ids(self) -> dict[str, Any]:
        """"""
        company_employers_ids = {}
        url = f"{self.BASE_URL}/employers"
        params = {
            "text": self._company_name,
            "per_page": 100,
        }
        data = self._make_request(url, params=params, headers=self.HEADERS)

        if len(data["items"]) > 0:
            pages = data["pages"]

            for page_num in range(pages):
                params["page"] = page_num
                data = self._make_request(url, params=params, headers=self.HEADERS)

                for employer in data["items"]:
                    if employer["open_vacancies"] != 0:
                        company_employers_ids[employer["id"]] = employer["name"]
                        print(f"{employer["name"]} ({employer["id"]}): вакансий - {employer["open_vacancies"]}.")
                    else:
                        continue

        return company_employers_ids


if __name__ == '__main__':
    api = HeadHunterApi("Yandex", "Python", "2")
    vacancies = api.get_employers_vacancies("1740")
    print(vacancies)
    print(len(vacancies))

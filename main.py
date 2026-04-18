import time

from src.hhapi import HeadHunterApi
from src.mockapi import MockApi

COMPANIES = {
    "Yandex": "1740",
    "VK": "15478",
    "Sber": "3529",
    "Tinkoff": "78638",
    "Ozon": "2180",
    "Alfa Bank": "80",
    "VTB": "4181",
    "MTS": "3776",
    "Tele2": "1122462",
    "Kaspersky": "1057"
}

FALLBACK_COMPANIES = {
    "Yandex": "1740",
    "VK": "15478",
    "Sber": "3529"
}


def is_api_available(working_api: HeadHunterApi) -> bool:
    try:
        working_api.get_employers_vacancies("1740")
        return True
    except Exception:
        return False


if __name__ == "__main__":
    api = HeadHunterApi("2")

    if not is_api_available(api):
        print("HH API недоступен, используем MOCK данные")
        api = MockApi()

    companies = COMPANIES if isinstance(api, HeadHunterApi) else FALLBACK_COMPANIES

    vacancies = {}

    for name, employer_id in companies.items():
        print(f"Загружаем вакансии для {name}...")

        try:
            vacancies[name] = api.get_employers_vacancies(employer_id)
        except Exception as e:
            print(f"Ошибка для {name}: {e}")
            vacancies[name] = []

        time.sleep(1)

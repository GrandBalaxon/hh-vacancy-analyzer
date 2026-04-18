import time

from src.api import HeadHunterApi

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


if __name__ == '__main__':
    api = HeadHunterApi("Python", "2")
    vacancies = {}

    for name, employer_id in COMPANIES.items():
        vacancies[name] = api.get_employers_vacancies(employer_id)
        time.sleep(1)

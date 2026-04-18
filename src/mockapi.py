from src.base_api import VacancyAPI


class MockApi(VacancyAPI):
    def get_employers_vacancies(self, employer_id: str) -> list[dict]:
        data = {
            "1740": [  # Yandex
                {
                    "id": "132167779",
                    "name": "Стажер-разработчик бэкенда (C++, Python)",
                    "salary": None,
                    "alternate_url": "https://hh.ru/vacancy/132167779",
                    "employer": {"id": "1740", "name": "Яндекс"},
                    "area": {"id": "66", "name": "Нижний Новгород"},
                    "snippet": {
                        "requirement": "Знание Python или C++",
                        "responsibility": "Разработка сервисов"
                    },
                    "schedule": {"id": "fullDay", "name": "Полный день"},
                    "experience": {"id": "noExperience", "name": "Нет опыта"},
                },
                {
                    "id": "132167780",
                    "name": "Python Backend Developer (Сервисы поиска)",
                    "salary": {"from": 200000, "to": 350000},
                    "alternate_url": "https://hh.ru/vacancy/132167780",
                    "employer": {"id": "1740", "name": "Яндекс"},
                    "area": {"id": "1", "name": "Москва"},
                    "snippet": {
                        "requirement": "Python, Django/FastAPI",
                        "responsibility": "Разработка backend сервисов"
                    },
                    "schedule": {"id": "fullDay", "name": "Полный день"},
                    "experience": {"id": "between1And3", "name": "1–3 года"},
                },
                {
                    "id": "132167781",
                    "name": "Data Engineer",
                    "salary": {"from": 250000, "to": 400000},
                    "alternate_url": "https://hh.ru/vacancy/132167781",
                    "employer": {"id": "1740", "name": "Яндекс"},
                    "area": {"id": "2", "name": "Санкт-Петербург"},
                    "snippet": {
                        "requirement": "SQL, Python, Spark",
                        "responsibility": "Пайплайны данных"
                    },
                    "schedule": {"id": "remote", "name": "Удалённая работа"},
                    "experience": {"id": "between3And6", "name": "3–6 лет"},
                },
            ],

            "15478": [  # VK
                {
                    "id": "232167779",
                    "name": "Backend Developer (Python, Django)",
                    "salary": {"from": 180000, "to": 300000},
                    "alternate_url": "https://hh.ru/vacancy/232167779",
                    "employer": {"id": "15478", "name": "VK"},
                    "area": {"id": "1", "name": "Москва"},
                    "snippet": {
                        "requirement": "Python, Django, PostgreSQL",
                        "responsibility": "Разработка API"
                    },
                    "schedule": {"id": "fullDay", "name": "Полный день"},
                    "experience": {"id": "between1And3", "name": "1–3 года"},
                },
                {
                    "id": "232167780",
                    "name": "Python Developer (Highload)",
                    "salary": {"from": 250000, "to": 420000},
                    "alternate_url": "https://hh.ru/vacancy/232167780",
                    "employer": {"id": "15478", "name": "VK"},
                    "area": {"id": "2", "name": "Санкт-Петербург"},
                    "snippet": {
                        "requirement": "Async Python, Redis, Kafka",
                        "responsibility": "Высоконагруженные сервисы"
                    },
                    "schedule": {"id": "remote", "name": "Удалённая работа"},
                    "experience": {"id": "between3And6", "name": "3–6 лет"},
                },
                {
                    "id": "232167781",
                    "name": "Frontend Developer (React)",
                    "salary": {"from": 150000, "to": 250000},
                    "alternate_url": "https://hh.ru/vacancy/232167781",
                    "employer": {"id": "15478", "name": "VK"},
                    "area": {"id": "1", "name": "Москва"},
                    "snippet": {
                        "requirement": "React, TypeScript",
                        "responsibility": "UI разработка"
                    },
                    "schedule": {"id": "fullDay", "name": "Полный день"},
                    "experience": {"id": "between1And3", "name": "1–3 года"},
                },
            ],

            "3529": [  # Sber
                {
                    "id": "332167779",
                    "name": "Python Developer (Fintech)",
                    "salary": {"from": 170000, "to": 310000},
                    "alternate_url": "https://hh.ru/vacancy/332167779",
                    "employer": {"id": "3529", "name": "Сбер"},
                    "area": {"id": "1", "name": "Москва"},
                    "snippet": {
                        "requirement": "Python, REST API",
                        "responsibility": "Финансовые сервисы"
                    },
                    "schedule": {"id": "fullDay", "name": "Полный день"},
                    "experience": {"id": "between1And3", "name": "1–3 года"},
                },
                {
                    "id": "332167780",
                    "name": "Data Scientist",
                    "salary": {"from": 220000, "to": 380000},
                    "alternate_url": "https://hh.ru/vacancy/332167780",
                    "employer": {"id": "3529", "name": "Сбер"},
                    "area": {"id": "2", "name": "Санкт-Петербург"},
                    "snippet": {
                        "requirement": "ML, Python, Pandas",
                        "responsibility": "Модели машинного обучения"
                    },
                    "schedule": {"id": "remote", "name": "Удалёнка"},
                    "experience": {"id": "between3And6", "name": "3–6 лет"},
                },
                {
                    "id": "332167781",
                    "name": "Java Developer",
                    "salary": {"from": 160000, "to": 270000},
                    "alternate_url": "https://hh.ru/vacancy/332167781",
                    "employer": {"id": "3529", "name": "Сбер"},
                    "area": {"id": "1", "name": "Москва"},
                    "snippet": {
                        "requirement": "Java, Spring",
                        "responsibility": "Backend разработка"
                    },
                    "schedule": {"id": "fullDay", "name": "Полный день"},
                    "experience": {"id": "between1And3", "name": "1–3 года"},
                },
            ],
        }

        return data.get(employer_id, [])
import logging
import psycopg2

logger = logging.getLogger("db_manager")


class DBManager:
    """"""

    def __init__(self):
        pass

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        pass

    def get_all_vacancies(self):
        """Метод для получения списка всех вакансий с указанием названия компании, названия вакансии и зарплаты и
        ссылки на вакансию."""
        pass

    def get_avg_salary(self):
        """Метод для получения средней зарплаты по вакансиям."""
        pass

    def get_vacancies_with_higher_salary(self):
        """Метод для получения списка всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    def get_vacancies_with_keyword(self):
        """Метод для получения списка всех вакансий, в названии которых содержатся переданные в метод слова
        (например python)."""
        pass

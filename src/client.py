import requests
# from src.auth.schemas import UserCreate
from config import api_url


def get_researches():
    """
    Получаем все опросы
    :return list:
    """
    return requests.get(f"{api_url}/researches/?research_title=%D0%9E%D0%BF%D1%80%D0%BE%D1%81%201").json()


def get_question_one():
    """
    Получаем вопрос 1
    :return list:
    """
    return requests.get(
        f"{api_url}/questions/?question_title=%D0%9A%D0%B0%D0%BA%20%D0%92%D1%8B%20%D1%83%D0%B7%D0%BD%D0%B0%D0%BB%D0%B8%20%D0%BE%20%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B8%20%D0%9A%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8%3F").json()


def get_question_two():
    return requests.get(
        f"{api_url}/questions/?question_title=%D0%9D%D0%B0%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82%D0%BB%D0%B8%D0%B2%D1%8B%20%D0%B1%D1%8B%D0%BB%D0%B8%20%D1%81%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%9A%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%B2%D0%BE%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F%20%D0%92%D0%B0%D1%88%D0%B5%D0%B3%D0%BE%20%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%B2%D0%B8%D0%B7%D0%B8%D1%82%D0%B0%20%D0%B2%20%D0%BE%D1%84%D0%B8%D1%81%20%D0%9A%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8%3F").json()


def get_question_three():
    return requests.get(
        f"{api_url}/questions/?question_title=%D0%9E%D1%86%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D1%84%D0%B5%D1%81%D1%81%D0%B8%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%D0%BC%20%D1%81%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D0%BA%D0%B0%2C%20%D0%B7%D0%B0%D0%BD%D0%B8%D0%BC%D0%B0%D0%B2%D1%88%D0%B5%D0%B3%D0%BE%D1%81%D1%8F%20%D0%92%D0%B0%D1%88%D0%B8%D0%BC%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%3A").json()


def get_question_four():
    return requests.get(
        f"{api_url}/questions/?question_title=%D0%9D%D0%B0%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20%D0%BF%D1%80%D0%BE%D0%B4%D0%BE%D0%BB%D0%B6%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%BC%20%D0%B1%D1%8B%D0%BB%D0%BE%20%D1%81%D0%BE%D0%B1%D0%B5%D1%81%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%20%D0%BD%D0%B8%D0%BC%20%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D1%8B%3F").json()


def get_question_five():
    return requests.get(
        f"{api_url}/questions/?question_title=%D0%94%D0%BE%D1%81%D1%82%D0%B0%D1%82%D0%BE%D1%87%D0%BD%D0%BE%20%D0%BB%D0%B8%20%D0%92%D0%B0%D1%81%20%D0%BF%D1%80%D0%BE%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%20%D0%BE%20%D0%9A%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8").json()


def get_question_six():
    return requests.get(
        f"{api_url}/questions/?question_title=%D0%9D%D0%B0%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20%D0%BF%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%BE%D0%B9%20%D0%B1%D1%8B%D0%BB%D0%B0%20%D0%B8%D0%BD%D1%84%D0%BE%D0%BC%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BE%D0%B1%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B5%D1%81%D1%83%D1%8E%D1%89%D0%B5%D0%B9%20%D0%92%D0%B0%D1%81%20%D0%B4%D0%BE%D0%BB%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D0%B8%3F").json()


def get_question_seven():
    return requests.get(
        f"{api_url}/questions/?question_title=%D0%9D%D0%B0%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20%D0%BF%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%BE%20%D0%92%D0%B0%D1%81%20%D0%BE%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D0%B8%D0%BB%D0%B8%20%D1%81%20%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%D0%BE%D0%BC%20%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%B0%20%D0%BD%D0%B0%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%83%3F").json()


def get_question_eight():
    return requests.get(
        f"{api_url}/questions/?question_title=%D0%9E%D1%86%D0%B5%D0%BD%D0%B8%D1%82%D0%B5%20%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D1%83%20%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%B0%20%D0%BD%D0%B0%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%83%20%D0%B2%20%D1%86%D0%B5%D0%BB%D0%BE%D0%BC%3A").json()

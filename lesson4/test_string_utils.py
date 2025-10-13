import pytest
from string_utils import StringUtils

def test_to_camel_case():
    utils = StringUtils()
    # Позитивные тесты
    assert utils.to_camel_case("hello world") == "helloWorld"
    assert utils.to_camel_case("one two three") == "oneTwoThree"
    assert utils.to_camel_case("Test") == "Test"  # Не пустая строка
    assert utils.to_camel_case("04 апреля 2023") == "04Апреля2023" # C пробелами

    # Негативные тесты
    assert utils.to_camel_case("") == ""  # Пустая строка
    assert utils.to_camel_case(" ") == ""  # Строка с пробелом
    assert utils.to_camel_case(None) == None if hasattr(utils, 'to_camel_case') and utils.to_camel_case(None) else True  # None

def test_to_snake_case():
    utils = StringUtils()
    assert utils.to_snake_case("helloWorld") == "hello_world"
    assert utils.to_snake_case("OneTwoThree") == "one_two_three"
    assert utils.to_snake_case("Test") == "test" #не пустая строka
    assert utils.to_snake_case("123") == "123" #числа как строка

    assert utils.to_snake_case("") == ""  # Пустая строка
    assert utils.to_snake_case(" ") == "_"  # Строка с пробелом
    assert utils.to_snake_case(None) == None if hasattr(utils, 'to_snake_case') and utils.to_snake_case(None) else True  # None

def test_count_vowels():
    utils = StringUtils()
    assert utils.count_vowels("hello") == 2
    assert utils.count_vowels("AEIOUaeiou") == 10
    assert utils.count_vowels("Тест") == 1 #Не пустая строка
    assert utils.count_vowels("123") == 0 #Числа как строка

    assert utils.count_vowels("sky") == 0
    assert utils.count_vowels("") == 0 #Пустая строка
    assert utils.count_vowels(" ") == 0 #Строка с пробелом
    assert utils.count_vowels(None) == None if hasattr(utils, 'count_vowels') and utils.count_vowels(None) else True # Проверка Nonе

def test_is_palindrome():
    utils = StringUtils()
    assert utils.is_palindrome("madam") == True
    assert utils.is_palindrome("Racecar") == True
    assert utils.is_palindrome("Тест") == False #Не пустая строка
    assert utils.is_palindrome("123") == False #Числа как строка

    assert utils.is_palindrome("hello") == False
    assert utils.is_palindrome("") == True #Пустая строка
    assert utils.is_palindrome(" ") == True #Строка с пробелом
    assert utils.is_palindrome(None) == None if hasattr(utils, 'is_palindrome') and utils.is_palindrome(None) else True # Проверка Nonе

def test_reverse_words():
    utils = StringUtils()
    assert utils.reverse_words("hello world") == "world hello"
    assert utils.reverse_words("one two three") == "three two one"
    assert utils.reverse_words("Тест") == "Тест" #Не пустая строка
    assert utils.reverse_words("04 апреля 2023") == "2023 апреля 04" #Строка с пробелами

    assert utils.reverse_words("single") == "single"
    assert utils.reverse_words("") == "" #Пустая строка
    assert utils.reverse_words(" ") == "" #Строка с пробелом
    assert utils.reverse_words(None) == None if hasattr(utils, "reverse_words") and utils.reverse_words(None) else True# Проверка Nonе

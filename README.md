
Разработаны автоматизированные тесты для учебного проекта Stellar Burgers с использованием Selenium и Pytest.
Проект включает автоматические тесты для проверки ключевых функций сайта Stellar Burgers:
    Регистрация и Авторизация
    - Успешная регистрация нового пользователя
    - Ошибка при некорректном пароле
    - Вход через кнопку "Войти в аккаунт"
    - Вход через кнопку "Личный кабинет"
    - Вход через форму регистрации
    - Вход через форму восстановления пароля
    - Выход из аккаунта

    Навигация
    - Переход в личный кабинет
    - Возврат в конструктор через кнопку
    - озврат в конструктор через логотип

    Конструктор бургеров
    - Переход к разделу "Булки"
    - Переход к разделу "Соусы"
    - Переход к разделу "Начинки"

 Структура проекта тестирования сервиса Stellar Burgers, включет 
    Файлы: 
    - conftest.py с использованными фикстурами, 
    - data.py с URL,  
    - helpers.py с генератором логина в форме email
    - .gitignore с исключениями для Git
    Папки:
    - locators с постраничными локаторами, 
    - tests с автотестами по классам:
        - регистрация (class TestRegistration)
        - вход (class TestLogin)
        - перходы в личный кабинет и из него (class TestNavigation)
        - выход из аккаунта(test_logout_from_personal_account)
        - переходы по по разделам конструктора(class TestConstructor)

Технологии:
- Браузер Google Chrome: Версия: 141.0.7390.66
- Python 
- Selenium WebDriver
- Pytest
- Chrome Driver

Автотесты проходили проверку в бруазере Chrome с разрешением экрана 2560*1440.  
Все тесты проходят успешно.

Отчет о прверке pytest:
Все тесты прошли успешно.
collected 13 items

tests/test_constructor.py::TestConstructor::test_constructor_sauces_section PASSED                              [  7%]
tests/test_constructor.py::TestConstructor::test_constructor_fillings_section PASSED                            [ 15%]
tests/test_constructor.py::TestConstructor::test_constructor_buns_section PASSED                                [ 23%]
tests/test_login.py::TestLogin::test_login_from_main_page_button PASSED                                         [ 30%]
tests/test_login.py::TestLogin::test_login_from_personal_account_button PASSED                                  [ 38%]
tests/test_login.py::TestLogin::test_login_from_registration_form PASSED                                        [ 46%]
tests/test_login.py::TestLogin::test_login_from_password_recovery_form PASSED                                   [ 53%]
tests/test_logout.py::test_logout_from_personal_account PASSED                                                  [ 61%]
tests/test_navigation.py::TestNavigation::test_navigate_to_personal_account PASSED                              [ 69%]
tests/test_navigation.py::TestNavigation::test_navigate_from_personal_account_to_constructor_via_button PASSED  [ 76%]
tests/test_navigation.py::TestNavigation::test_navigate_from_personal_account_to_constructor_via_logo PASSED    [ 84%]
tests/test_registration.py::TestRegistration::test_successful_registration PASSED                               [ 92%]
tests/test_registration.py::TestRegistration::test_registration_invalid_password PASSED                         [100%]

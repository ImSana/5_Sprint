from selenium.webdriver.common.by import By

class TestLocators:
    PERSONAL_ACCOUNT_BUTTON = By.LINK_TEXT, \
        "Личный Кабинет"  # Кнопка «Личный Кабинет»
    LINK_REGISTRATION = By.LINK_TEXT, \
        "Зарегистрироваться"  # Ссылка на форму регистации
    NAME_FIELD = By.XPATH, \
        '//*[text()="Имя"]/following-sibling::input'  # Поле ввода имени
    EMAIL_FIELD = By.XPATH, \
        '//*[text()="Email"]/following-sibling::input'  # Поле ввода почты
    PASSWORD_FIELD = By.XPATH, \
        '//*[text()="Пароль"]/following-sibling::input'  # Поле ввода пароля
    REGISTRATION_BUTTON = By.XPATH,\
        '//*[contains(@class, "button_button_type_primary")]'  # Кнопка "Зарегистрироваться"
    ERROR_REGISTRATION = By.XPATH, \
        '//*[contains(@class, "input__error text_type_main-default")]'  # Ошибка регистрации

    ORDER_BUTTON = By.XPATH, \
        '//*[contains(@class, "button_button_type_primary") and contains(text(), "Оформить заказ")]'  # Кнопка заказа
    ENTER_LINK = By.LINK_TEXT, \
        "Войти"  # Ссылка на форму авторизации
    ENTER_IN_ACCOUNT_BUTTON = By.XPATH, \
        '//*[text()="Войти в аккаунт"]'  # Кнопка «Войти в аккаунт»
    ENTER_BUTTON = By.XPATH, \
        '//*[contains(@class, "button_button_type_primary") and contains(text(), "Войти")]'  # Кнопка «Войти»
    RECOVERY_LINK = By.LINK_TEXT, \
        "Восстановить пароль"  # Ссылка на форму восстановления

    ACCOUNT_MENU = By.XPATH,\
        '//*[contains(@class, "Account_list_")]'  # Меню личного кабинета

    CONSTRUCTOR_TAB = By.XPATH,\
        '//*[contains(@class, "AppHeader_header") and contains(text(), "Конструктор")]'  # Вкладка «Конструктор»
    INGREDIENTS_HEADER = By.XPATH,\
        '//*[contains(@class, "BurgerIngredients") ]/child::h1[contains(@class, "text")]'  # Заголовок ингредиентов
    LOGO_BUTTON = By.XPATH,\
        '//*[contains(@class, "AppHeader_header__logo")]'  # Кнопка логотипа

    LOGOUT_BUTTON = By.XPATH, \
        '//*[text()="Выход"]'  # Кнопка «Выход»

    UNSELECTED_INGREDIENT_TABS = By.XPATH,\
        '//*[contains(@class, "tab_tab") and not(contains(@class, "current"))]/child::span'  # Невыбранные вкладки
    SELECTED_INGREDIENT_TAB = By.XPATH,\
        '//*[contains(@class, "tab_tab") and contains(@class, "current")]/child::span'  # Выбранная вкладка
    BUNS_TUB = By.XPATH,\
        "//span[text()='Булки']/parent::*"  # Вкладка булок
    SAUCES_TUB = By.XPATH, \
        '//span[text()="Соусы"]/parent::*'  # Вкладка соусов
    FILLINGS_TUB = By.XPATH, \
        "//span[text()='Начинки']/parent::*"  # Вкладка начинок
    BUNS_HEADER = By.XPATH, \
        '//*[contains(@class, "text text_type_main-medium") and contains(text(), "Булки")]'  # Заголовок булок
    FILLINGS_HEADER = By.XPATH, \
        '//*[contains(@class, "text text_type_main-medium") and contains(text(), "Начинки")]'  # Заголовок начинок


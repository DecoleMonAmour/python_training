from fixture.application import Application
import pytest

# Функция для создания фикстуры

fixture = None  # переменная для хранения наличия фикстуры
# @pytest.fixture(scope="session")  # добавили scope, чтобы фикстура создавалась один раз, и все тесты ею пользовались. Это дает оптимизацию по скорости, но если браузер в какой-то момент упадет, все последующие тесты провалятся
@pytest.fixture  # перед каждым тестом создается своя фикстура. Падение браузера в одном тест-кейсе не завалит другие. Но для оптимизации добавим проверку - если уже фикстура есть, новая создаваться не будет
def app(request):
    # инициализация фикстуры
    global fixture
    if fixture is None:  # если фикстуры нет, создаем новую
        fixture = Application()  # создает фикстуру (объект типа Application)
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():  # если фикстура испорчена, создаем новую
            fixture = Application()  # создает фикстуру (объект типа Application)
            fixture.session.login(username="admin", password="secret")
    # возврат фикстуры
    return fixture


# функция для финализации фикстуры. Она будет отпрабатывать один раз и в самом конце
@pytest.fixture(scope="session", autouse=True)  # autouse=True позволяет фикстуре сработать автоматически, даже если она не указана ни у какого теста
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)  # указание на то, как эта фикстура должна быть разрушена
    return fixture
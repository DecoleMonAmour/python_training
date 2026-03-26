from fixture.application import Application
import pytest


@pytest.fixture(scope="session")  # добавили scope, чтобы фикстура создавалась один раз, и все тесты ею пользовались
def app(request):
    fixture = Application()  # создает фикстуру (объект типа Application)
    request.addfinalizer(fixture.destroy)  # указание на то, как эта фикстура должна быть разрушена
    return fixture
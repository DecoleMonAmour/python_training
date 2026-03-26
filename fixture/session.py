
class SessionHelper:  # помощник по работе с сессией

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd   # инициализировать драйвер не будем, тк он инициализируется при создании фикстуры
        self.app.open_home_page()
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element("link text", "Logout").click()


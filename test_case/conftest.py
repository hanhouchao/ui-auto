from page_object.login_page import LoginPage
from common import settings
import pytest


@pytest.fixture(scope="session", autouse=False)
def login():
    login_driver = LoginPage()
    try:
        login_driver.open()
        login_driver.type_admin()
        login_driver.type_username(settings.USERNAME)
        login_driver.type_password(settings.PASSWORD)
        login_driver.type_login()
        assert login.login_success(), "登录失败"
    except Exception as e:
        login_driver.quit()
        raise e
    yield login_driver
    login_driver.quit()

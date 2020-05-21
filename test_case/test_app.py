from page_object.application.app_create import AppCreatePage


class TestCreateApp():

    def 测试创建应用(self, browser):
        create_page = AppCreatePage(browser)
        create_page.open_create_app()
        create_page.create_app()

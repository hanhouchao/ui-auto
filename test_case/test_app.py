from page_object.application.app_create import AppCreatePage


class TestCreateApp():
    def setup_class(self):
        self.create_page = AppCreatePage()
        self.create_page.open_create_app()

    def test_create_app(self):
        self.create_page.create_app()

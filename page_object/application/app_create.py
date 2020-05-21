from page_object.page_base import BasePage


class AppCreatePage(BasePage):

    def open_create_app(self):
        self.open("console-acp/workspace;project=e2eproject;cluster=high;namespace=e2enamespace/app/list")

    def input_image(self):
        self.get_element_by_text("输入", type="span").click()
        self.fill_form({"镜像地址": "index.alauda.cn/alaudaorg/qaimages:helloworld"})

    def create_app(self):
        self.get_element_by_text("创建应用").click()
        self.input_image()

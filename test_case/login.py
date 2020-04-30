from page_object.login_page import LoginPage


# 创建test_user_login()函数
def test_user_login():
    """测试用户名/密码是否可以登录"""
    username = "954xxx"
    password = "xxxxxx"
    login_page = LoginPage()
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_login()
    login_page.quit()

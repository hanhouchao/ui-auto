# 创建test_user_login()函数
def test_user_login(login):
    assert login.login_success(), "登录失败"

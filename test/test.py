from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()

driver.get("https://netpeak.ua")
#Нажать на кнопку о нас
about_us = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]")
about_us.click()
driver.implicitly_wait(5)

#Нажать на кнопку команда
element_team = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div"
                                            "/nav/div[3]/div/div[2]/ul[1]/li[3]/div")
element_team.click()
driver.implicitly_wait(5)

#Нажать на кнопку стать частью команды
element_become_piece_of_team = driver.find_element_by_xpath("/html/body/div[1]/div[9]/div/div/div[10]/a")
element_become_piece_of_team.click()
driver.implicitly_wait(5)

driver.switch_to.window(driver.window_handles[1])
#Убедится что на странице есть кнопка "Я хочу работать в Netpeak"
element_i_want = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/a")
if element_i_want.is_enabled():
    element_i_want.click()
else:
    pass
    element_i_want.click()
    print("Element is active")
driver.implicitly_wait(5)
driver.close()

driver.switch_to.window(driver.window_handles[0])
#Нажать кнопку личный кабинет
my_cabinet = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/"
                                          "div/nav/div[1]/div[2]/ul/li[1]/a")
my_cabinet.click()
driver.implicitly_wait(5)

driver.switch_to.window(driver.window_handles[1])

#Заполнить логин и пароль
cabinet_login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/"
                                             "div[1]/md-input-container/input")

cabinet_login.send_keys("test")

driver.implicitly_wait(5)

cabinet_password = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/"
                                                "div[2]/md-input-container/input")
cabinet_password.send_keys("1111")
driver.implicitly_wait(5)

#Проверить что кнопка не доступна
button_login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div[5]/button")
if button_login.isDisable():
    button_login.click()
else:
    pass
    print("Element isn`t active")
driver.implicitly_wait(5)

#Отметить чекбокс
checkbox_policy = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div/md-checkbox")
checkbox_policy.click()
driver.implicitly_wait(5)

#Нажать на кнопку войти и проверить наличие нотификации об ошибке
button_login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div[5]/button")
button_login.click()
driver.implicitly_wait(5)

login_error = driver.find_element_by_xpath("/html/body/md-toast")
if login_error.is_displayed():
    print("Alert")

#Проверить что логин и пароль подсветились красным
login_alert_red = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form"
                                               "/div[1]/md-input-container/input")

password_alert_red = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form"
                                                  "/div[2]/md-input-container/input")
if login_alert_red.is_displayed():
    print("Login field is red")

if password_alert_red.is_displayed():
    print("Password field is red")

driver.close()

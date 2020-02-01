#! python3
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10)
url1 = 'https://www.baidu.com'
url2 = 'https://bbs.hupu.com'
url3 = 'https://www.taobao.com'

# 可以用mitmproxy解除访问网站中针对 window.navigator.webdriver 的控制
# driver.get(url1)
# try:

# except:
#     pass


def autobaidu(url):
    driver.get(url)
    elem = driver.find_element_by_class_name('s_ipt')
    elem.send_keys('疫情')
    elem.submit()
    elem.send_keys("功夫")
    elem = driver.find_element_by_xpath(
        '/html/body/div[1]/div[5]/div[1]/div[3]/div[3]/h3/a')
    elem.click()


def autohupu(url):
    driver.get(url)
    elem = driver.find_element_by_class_name('btn-login')
    elem.click()
    elem = driver.find_element_by_id('J_username')
    elem.send_keys('gladiator16')
    passelem = driver.find_element_by_id('J_pwd')
    passelem.send_keys('maize15963')
    yzelem = driver.find_element_by_id('rectMask')
    yzelem.click()
    # loginelem = driver.find_element_by_id('J_submit')
    # loginelem.click()
    # elem.submit()

def autotaobao(url):
    driver.get(url)
    elem = driver.find_element_by_class_name('h')
    elem.click()
    switchelem = driver.find_element_by_id('J_Quick2Static')
    switchelem.click()
    elemuser = driver.find_element_by_id('TPL_username_1')
    elemuser.send_keys('18953269170')
    passelem = driver.find_element_by_id('TPL_password_1')
    passelem.send_keys('Maize15$')
    yzelem = driver.find_element_by_id('J_SubmitStatic')
    yzelem.click()
    driver.get_screenshot_as_file("D:\\python\\baidu_img.jpg")
try:
    autotaobao(url3)


except:
    print(e)
# finally:
    # print(ctime())
    # driver.quit()

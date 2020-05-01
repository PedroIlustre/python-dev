from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\ilustre\Desktop\geckodriver.exe')

        # //a[@href='/account/login/?source=auth_switcher']
        # //input[@name='username']
        # //input[@name='password']

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(5)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(9)
        self.curtir_fotos('campobom')


    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
        time.sleep(10)
        for i in range(1, 100):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_hrefs in pic_hrefs:
            driver.get(pic_hrefs)
            #driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]').click()
                time.sleep(20)
            except Exception as e:
                print(e)
                time.sleep(5)


ilustreBot = InstagramBot('ilustre.fotografia','seamous9wild')
ilustreBot.login()

        
        
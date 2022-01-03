# import chromedriver_autoinstaller
import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Function:
    def __init__(self):

        self.options = Options()
        self.options.add_argument("--disable-gpu")
        self.options.headless = True
        self.extension_id = None

    def get_extension_id(self):
        try:
            self.driver.install_addon(os.getcwd() + "\\PENGUIN\\extension\\touch-vpn@anchorfree.com.xpi", temporary=True)

            for i in range(10):
                time.sleep(0.5)
                if len(self.driver.window_handles) >= 2:
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    break

            self.driver.get('about:addons')
            time.sleep(0.5)
            self.driver.find_elements_by_class_name('category-name')[1].click()
            self.driver.find_element_by_tag_name('addon-card').find_element_by_class_name('more-options-button').click()
            self.driver.find_element_by_tag_name('addon-options').find_elements_by_tag_name('panel-item')[2].click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(0.5)
            self.extension_id = self.driver.current_url.split('/')[2]
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(0.5)
        except Exception:
            return 2


    def onVPN(self):
        try:
            self.driver.get('moz-extension://{0}/panel/index.html'.format(self.extension_id))
            self.driver.find_element_by_class_name('button.button--red.data-consent__accept-button').click()
            self.driver.find_element_by_class_name('location').find_element_by_tag_name('span').click()
            time.sleep(0.3)
            country = self.driver.find_element_by_id('Locations').find_element_by_class_name('list').find_elements_by_tag_name('div')
            for c in country:
                if c.text == 'United States':
                    c.click()
                    self.driver.find_element_by_id('ConnectionButton').click()
                    for i in range(10):
                        time.sleep(1)
                        if self.driver.find_element_by_id('ConnectionButton').find_element_by_class_name('title').text == 'Stop':
                            return 1
                        if i == 9:
                            return 0
        except Exception:
            return 2
    def Login(self):
        try:
            self.driver.get('https://accounts.spotify.com/login')
            self.driver.find_element_by_class_name('control-indicator').click()
            self.driver.find_element_by_id('login-username').send_keys(self.ID)
            self.driver.find_element_by_id('login-password').send_keys(self.PW)
            self.driver.find_element_by_id('login-button').click()

            for i in range(20):
                time.sleep(0.5)
                if self.driver.current_url.find('login') == -1:
                    return 1
                if i == 19:
                    return 0
        except Exception:
            return 2

    def ChangeCountry(self):
        try:
            self.driver.get('https://www.spotify.com/kr-ko/account/profile/')

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "country")))

            country = self.driver.find_element_by_id('country').find_elements_by_tag_name('option')

            for c in country:
                if c.get_attribute('value') == 'US':
                    c.click()
                    self.driver.find_element_by_class_name('ButtonLegacy__ButtonLegacyInner-o653de-0.buexIy.encore-bright-accent-set').click()
                    break
            

            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "EditProfile__StyledSection-sc-1vn1swb-0.gpnMDj")))
            return 1

        except Exception:
            return 2

if __name__ == '__main__':
    work = Control()
    work.onVPN()
    work.Login()
    work.ChangeCountry()
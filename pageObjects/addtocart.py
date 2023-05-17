import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Addtocart:
    def __init__(self,driver):
        self.driver=driver
    def AddToCart(self):
        Shooos= self.driver.find_elements(By.XPATH,"//div[@class='_1YokD2 _3Mn1Gg']")
        for shoo in Shooos:
            shoo.find_element(By.XPATH,"(//div)[266]").click()
        time.sleep(10)
        child_window = self.driver.window_handles[1]
        self.driver.switch_to.window(child_window)
        try:
            self.driver.find_element(By.XPATH,"//a[@class='_1fGeJ5 _2UVyXR _31hAvz']").click()
        except:
            pass
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2U9uOA ihZ75k _3AWRsL']").click()
        time.sleep(5)
        #=========Place order==================
        self.driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2ObVJD _3AWRsL']").click()
        #=========choose delivery address============
        self.driver.find_element(By.XPATH,"//button[@class='_2KpZ6l RLM7ES _3AWRsL']").click()
        time.sleep(5)




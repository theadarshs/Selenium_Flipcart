from selenium.webdriver.common.by import By


class Addtocart:
    def AddToCart(self):
        Shooos= self.driver.find_elements(By.XPATH,"//div[@class='_1YokD2 _3Mn1Gg']")
        for shoo in Shooos:
            shoo.find_element(By.XPATH,"(//div)[262]").click()

        windowsopen = self.driver.window_handles
        self.driver.switch_to.window(windowsopen[1])

        self.driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2U9uOA _3v1-ww']").click()




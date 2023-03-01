
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class prueba_Selenium(unittest.TestCase):

    def setUp(self) :
        print("me ejecuto antes de cada test")
        self.driver = webdriver.Chrome()
        time.sleep(3)
        pass

    def test_a(self) :
        print("me ejecuto antes de cada test A")
        #google
        self.driver.get("https://www.google.com")
    #buscamos wikipedia
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys("wikipedia")
        search_bar.send_keys(Keys.ENTER)

        #Busqueda de google
        self.driver.find_element(By.XPATH, "( //DIV[@id='search']/descendant:: div [@class='g'])[1]/descendant::a[1]").click()
        #Wikipedia
        title = self.driver.title
        
        self.assertEqual("Wikipedia, la enciclopedia libre", title)
        pass

    def tearDown(self):
        print("me ejecuto después de cada test")
        self.driver.quit()
        pass


if __name__== "__main__":
    unittest.main()
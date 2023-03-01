from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#opciones de navegacion

options = webdriver.ChromeOptions()
options.add_argument('--start-maximied')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome()
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)
driver.get("https://eltiempo.es")

WebDriverWait(driver,5)\
.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.didomi-components-button.didomi-button.didomi-dismiss-button.didomi-components-button--color.didomi-button-highlight.highlight-button')))\
.click()

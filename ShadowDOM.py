from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver.get("http://localhost:3000")
driver.find_element(By.LINK_TEXT, "ShadowDOM").click()
nodoShadowHost = driver.find_element(By.ID, "nodoShadowHost")
nodoShadowRoot = driver.execute_script("return arguments[0].ShadowRoot", nodoShadowHost)
nodoShadowRoot.find_element(By.ID, "boton2")
nodoShadowRoot.find_element(By.ID, "boton2").click()
nodoShadowRoot.find_element(By.ID, "result").text

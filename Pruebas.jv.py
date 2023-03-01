from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver.get("http://localhost:3000")
driver.find_element(By.LINK_TEXT, "XPaths").click() 
botones = driver.find_elements(By.TAG_NAME, "button")
len(botones)
botones[10].location["y"]
driver.execute_script("window.scrollBy(0, arguments[0])",botones[10].location["y"])
driver.execute_script("alert('Error')")
driver.switch_to.alert.accept()

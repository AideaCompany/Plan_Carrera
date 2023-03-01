from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.get('https://www.google.com/webhp?hl=es-419&sa=X&ved=0ahUKEwj3mPDrm8z8AhWhRDABHbgXAlwQPAgI')

driver.get("https://es.wikipedia.org")
driver.find_element(By.TAG_NAME, "title")
driver.find_element(By.TAG_NAME, "title").get_attribute("textContent")
title=driver.title
title
driver.quit()
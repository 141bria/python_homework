from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
driver.get("https://en.wikipedia.org/wiki/Web_scraping")
print(driver.title)
driver.quit()

see_also = driver.find_element(
    By.CSS_SELECTOR, '[id="See_also"]'
)
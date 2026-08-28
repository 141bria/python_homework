import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/Top10/2025/")
top_10_2025_list = driver.find_element(By.CSS_SELECTOR,'[id="top-102025-list"]')
links=[]
if (top_10_2025_list):
    parent_div = top_10_2025_list.find_element(By.XPATH,'..')
    top_10_ol = top_10_2025_list.find_element(By.XPATH,'following-sibling::ol')
    vulnerability_title = top_10_ol.text
    for item in top_10_ol.find_elements(By.XPATH,'li'):
        a_tag = item.find_element(By.TAG_NAME,"a")
        href_link = a_tag.get_attribute("href")
        vulnerabilities = {"Title":item.text,"Link":href_link}
        links.append(vulnerabilities)
print(links)
with open("owasp_top_10.csv","w",newline='') as file:
    writer = csv.DictWriter(file,fieldnames=["Title","Link"])
    writer.writeheader()
    writer.writerows(links)
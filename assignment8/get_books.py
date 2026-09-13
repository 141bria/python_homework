from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

import pandas as pd
import json

search_result= driver.find_elements(By.CSS_SELECTOR,'li.cp-search-result-item')
results = []
for book in search_result:
    title = book.find_element(By.CSS_SELECTOR,'.title-content')
    authors = book.find_elements(By.CSS_SELECTOR,'.author-link')
    author_names = [author.text for author in authors]
    book_format = book.find_elements(By.CSS_SELECTOR, '.bib-details')
    author_names = ";".join(author_names)
    book_details = {"Title": title.text,
                "Author": author_names,
                "Format-Year": book_format[0].text if book_format else ""}
    results.append(book_details)
book_df = pd.DataFrame(results)
print(book_df)
driver.quit()

book_df.to_csv("get_books.csv")
with open("get_books.json","w") as file:
    json.dump(results,file)
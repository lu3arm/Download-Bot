import selenium
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print()
print("DOWNLOAD-BOTTER")
print()
starget = int(input("TARGET-DOWNLOAD.AMOUNT: "))
stargetadr = input("TARGET-WEB.DOWNLOAD.ADRES: ")
stargetdwnl = input("/Users/ *USER* /Downloads/ *FILE_NAME*  - so the downloaded files get deleted: ")
file_path = stargetdwnl
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 3)
visible = EC.visibility_of_element_located
browser.get(stargetadr)
for x in range(starget):
    time.sleep(14)                     # CHANGE HERE - FASTER BUT COULD CAUSE DATA TRASH
    if os.path.exists(file_path):
        os.remove(file_path)
    browser.refresh()
    time.sleep(10)                    # CHANGE HERE - FASTER BUT COULD CAUSE DATA TRASH
    if os.path.exists(file_path):
        os.remove(file_path)
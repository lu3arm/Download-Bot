#IMPORTING-MODULES
try:
    import selenium
    import time, os, platform
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except:
    print()
    print("ERROR!")
    print("Error while importing modules. Please install the modules in requirements.txt")
    input("Press Enter to Exit ")
    quit()

#TITLE
print("""
  _____   ______          ___   _ _      ____          _____             ____   ____ _______ 
 |  __ \ / __ \ \        / / \ | | |    / __ \   /\   |  __ \           |  _ \ / __ \__   __|
 | |  | | |  | \ \  /\  / /|  \| | |   | |  | | /  \  | |  | |  ______  | |_) | |  | | | |   
 | |  | | |  | |\ \/  \/ / | . ` | |   | |  | |/ /\ \ | |  | | |______| |  _ <| |  | | | |   
 | |__| | |__| | \  /\  /  | |\  | |___| |__| / ____ \| |__| |          | |_) | |__| | | |   
 |_____/ \____/   \/  \/   |_| \_|______\____/_/    \_\_____/           |____/ \____/  |_|                                                                            
  """)

if platform.system() == "Windows":
    clear = "cls"
else:
    clear = "clear"

print()
print("DOWNLOAD-BOT by KingfernJohn")
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
time.sleep(15)
browser.quit()
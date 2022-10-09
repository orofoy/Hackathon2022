from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Disables notifications when opening
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get("https://www.opensubtitles.org/en/search/sublanguageid-all")

search = driver.find_element(By.NAME, "MovieName")

search.send_keys("Star Wars: Episode")
search.send_keys(Keys.RETURN)


try:

    body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search_results"))
    )
    movieLink = body.find_element(By.CLASS_NAME, "bnone")
    movieLink.click()

    # try:
    #     languages = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "subtitle-language-selector-link"))
    #     )
    languages = driver.find_element(By.ID, "subtitle-language-selector-link")
    languages.click()

    english = driver.find_element(By.ID, "wl_en")
    english.click()

    buttonSet = body.find_element(By.CLASS_NAME, "ui-dialog-buttonset")
    #okButton = buttonSet.find_element(By.CLASS_NAME, "ui-button-text")
    buttonSet.click()
    #     languages.click()
    #ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only
    #     try:
    #         english = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.ID, "wl_en"))
    #         )
    #         english.click()
    #
    #         try:
    #             subs = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.ID, "subtitles_body"))
    #             )
    #
    #
    #         except:
    #             print("xd")
    #     except:
    #         print("lore")
    #     #languageSelector = results.find_element(By.ID, "subtitle-language-selector-link")
    #     #languageSelector.click()
    #     #for element in trs:
    #         #if element.title == "English":
    #             #languageLink = element.find_element(By.CLASS_NAME, "bnone")
    #             #languageLink.click()
    #             #break
    # except:
    #     print("test!!!")
    #
    # #elements = body.find_elements(By.TAG_NAME, "tr")
    # #for link in elements:
    #
    # #movieLink.click()
    #     #time.sleep(3)
    #    # driver.back()
    # #driver.back()
except:
    print("test?")



    #print(movieLink.text)
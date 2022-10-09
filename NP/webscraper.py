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

search = driver.find_element_by_name("MovieName")
#search = driver.find_element_by_class_name()

search.send_keys("Star Wars")
search.send_keys(Keys.RETURN)

try:
    body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "subtitles_body"))
    )

    content = body.find_elements_by_class_name("content")
    results = content.find_elements_by_id("search_results")
    time.sleep(5)
   # print(results.text)
except:
    driver.quit()


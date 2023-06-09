#---Data Entry Job Automation Project---#

from selenium import webdriver
from selenium.webdriver.common.by import By
from Website_Scraping import Scraping
# WEBDRIVER going to be driving the Chrome Browser and doing all our automated tasks.

chrome_driver_path = "/Users/siddharthmishra/Desktop/Siddharth/For_selenium_work/chromedriver"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfbI0_1sbEFDOmtGFvQ6NyqzQR_ZYhkNfZ4hWFL_8_evf29Aw/viewform?usp=sf_link"

scraping = Scraping()
print(scraping.all_price)
print(scraping.all_addresses)
print(scraping.all_links)
class Google_fill:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)


    def fill_google_form(self):
        for i in range(len(scraping.all_links)):
            self.driver.get(GOOGLE_FORM_URL)
            self.all_questions = self.driver.find_elements(By.CSS_SELECTOR, ".whsOnd")
            if i > (len(scraping.all_addresses)-1):
                pass
            else:
                self.all_questions[0].send_keys(scraping.all_addresses[i])
            if i > (len(scraping.all_price)-1):
                pass
            else:
                self.all_questions[1].send_keys(scraping.all_price[i])
            self.all_questions[2].send_keys(scraping.all_links[i])
            submit_button = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
            submit_button.click()


google = Google_fill()
google.fill_google_form()


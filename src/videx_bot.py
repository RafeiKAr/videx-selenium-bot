
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class VidexBot:
    def init(self, download_path):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": download_path,
            "download.prompt_for_download": False
        })
        self.driver = webdriver.Chrome(options=options)

    def open_page(self):
        self.driver.get("https://videx.diplo.de/videx/visum-erfassung/videx-kurzfristiger-aufenthalt")
        time.sleep(3)

    def fill_text(self, element_id, value):
        el = self.driver.find_element(By.ID, element_id)
        el.clear()
        el.send_keys(value)
        time.sleep(0.2)

    def quit(self):
        self.driver.quit()
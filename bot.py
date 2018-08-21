from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess, sys
from selenium import common

def run_bot():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    # chrome_options.add_argument("user-data-dir=C:\\Users\\Mpak\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http://streambooster.ru/')
    # Авторизуемся
    login_button = driver.find_element_by_xpath("//a[text()='Авторизоваться']")
    login_button.click()
    twitch_log_button = driver.find_element_by_xpath("//a[@id='oauth-trigger']")
    twitch_log_button.click()



if __name__ == '__main__':
    run_bot()
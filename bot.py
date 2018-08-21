from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess, sys
from selenium import common

def run_bot():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("user-data-dir=C:\\Users\\Mpak\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http://streambooster.ru/')
    # # Авторизуемся
    # login_button = driver.find_element_by_xpath("//a[text()='Авторизоваться']")
    # login_button.click()
    # time.sleep(3)
    # twitch_auth_button = driver.find_element_by_xpath("//a[@id='oauth-trigger']")
    # twitch_auth_button.click()

    # tw_username = driver.find_element_by_id("username")
    # tw_username.send_keys("log")
    # tw_pass = driver.find_element_by_xpath("//input[@name='password']")
    # tw_pass.send_keys("pass")
    # tw_log_button = driver.find_element_by_xpath("//span[@class='js-login-text']")
    # tw_log_button.click()
    # time.sleep(10)


if __name__ == '__main__':
    run_bot()

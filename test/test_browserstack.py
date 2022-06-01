import pytest
from selenium import webdriver
from src.pages.homepage import Homepage
from src.pages.sign_up_page import SignUpPage
from webdriver_manager.chrome import ChromeDriverManager

def test_browserstack():
   driver = webdriver.Chrome(ChromeDriverManager().install())
   driver.get("https://www.bstackdemo.com/")

   homepage = Homepage(driver)
   sign_up_page = SignUpPage(driver)

   sign_up_page.click_on_signin()
   sign_up_page.enter_username()
   sign_up_page.enter_password()
   sign_up_page.click_on_login()

   homepage.get_username()
   
   driver.quit()

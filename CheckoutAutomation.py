from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#Initiate the browser

browser = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.saucedemo.com/'


#Open the Website
browser.get(URL)



#Login 
browser.find_element(By.ID,'user-name').send_keys('standard_user')
browser.find_element(By.ID,'password').send_keys('secret_sauce')

browser.find_element(By.ID,'login-button').click();

#Select the Product
browser.find_element(By.ID,'add-to-cart-sauce-labs-backpack').click();

#Acces Cart and Checkout
browser.find_element(By.CLASS_NAME,'shopping_cart_link').click();
browser.find_element(By.ID,'checkout').click();

#Input Checkout information and complete purchase

browser.find_element(By.ID,'first-name').send_keys('JUAN')
browser.find_element(By.ID,'last-name').send_keys('Perez')
browser.find_element(By.ID,'postal-code').send_keys('33195')
browser.find_element(By.ID,'continue').click()
browser.find_element(By.ID,'finish').click()

#Navigate back to products screen
browser.find_element(By.ID,'back-to-products').click()








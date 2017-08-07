from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Instantiating Chrome webdriver and navigating to login page
driver = webdriver.Chrome()
driver.get('<Login Page for User(sensitive)>')

#Grabbing the username and password text box fields from DOM
user_textbox = driver.find_element_by_id('username')
password_textbox = driver.find_element_by_name('password')

#Filling in your username and password into fields
user_textbox.clear()
user_textbox.send_keys('<Username (sensitive)>')

password_textbox.clear()
password_textbox.send_keys('<Password (sensitive)>')
#Return key sent to login
password_textbox.send_keys(Keys.RETURN)

#<-------LOGGED IN NOW------------->

#Click on that display element!
driver.find_element_by_link_text('Real-time Display').click()
#Find and grab feed in power
feed_in_power = driver.find_element_by_xpath("(//div[@class='innerText'])[2]").text
numeric_feed_in_power = int(feed_in_power[:-1])
print(numeric_feed_in_power)

#If greater than 1500, trigger switch
if numeric_feed_in_power > 1500:
	driver.get('<trigger switch URL and key (sensitive)>')
#If less than -500, turn off switch
if numeric_feed_in_power < -500:
	driver.get('<turn off switch URL and key (sensitive)>')

#Closes the driver window
self.driver.close()

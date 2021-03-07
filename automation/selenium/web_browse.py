from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
message_field = driver.find_element_by_xpath('//*[@id="user-message"]')
message_field.send_keys('Cesar')
show_message_button = driver.find_element_by_xpath('//*[@id="get-input"]/button')
show_message_button.click()

# Two field form
a_field = driver.find_element_by_xpath('//*[@id="sum1"]')
b_field = driver.find_element_by_xpath('//*[@id="sum2"]')

a_field.send_keys('11')
b_field.send_keys('171')

total_button = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
total_button.click()
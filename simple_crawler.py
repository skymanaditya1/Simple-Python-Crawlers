from selenium import webdriver
from selenium.webdriver.common.keys import Key
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://www.w3c.org')
element = driver.find_element_by_name('q')
element.send_keys('hi mom')

element_text = element.text
element_attribute_value = element.get_attribute('value')

print(element)
print('element.text: {0}'.format(element_text))
print('element.get_attribute(\'value\'): {0}'.format(element_attribute_value))
driver.quit()

import selenium

print("Loading")

from selenium import webdriver
url = '##Input URL##'
driver = webdriver.Firefox(
    executable_path=r'/##InputWeb Driver File Path##'
)
driver.get(url)
driver.maximize_window()

Price = driver.find_element_by_xpath('##Xpath Location')
matches = driver.find_elements_by_tag_name('li')
for match in matches:
    print (match.text)

#confirm works !!!!!

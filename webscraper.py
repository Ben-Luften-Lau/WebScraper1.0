import selenium

print("Loading")

from selenium import webdriver
url = 'https://www.iproperty.com.my/sale/penang/all-residential/'
driver = webdriver.Firefox(
    executable_path=r'/home/northon_polaris/geckodriver'
)
driver.get(url)
driver.maximize_window()

Price = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/ul/li[1]/div/div/div[3]/div[1]/ul/li')
matches = driver.find_elements_by_tag_name('li')
for match in matches:
    print (match.text)

#confirm works !!!!!

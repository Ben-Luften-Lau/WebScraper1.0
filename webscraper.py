import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
print("Loading")

#   Replace: ### with correct data
url = '###Replace url '
driver = webdriver.Firefox(
    executable_path=r'###'
)
driver.get(url)
driver.maximize_window()
#   Find 2 items
#  Listingprice
Listingprice = driver.find_elements(
    by=By.XPATH, value="###")
Listingprice_list = []

for Lprice in range(len(Listingprice)):
    Listingprice_list.append(Listingprice[Lprice].text)


#   Price per square feet
PricePSqft = driver.find_elements(
    by=By.XPATH, value='###')
PricePSqft_list = []

for L_PricePSqft in range(len(PricePSqft)):
    PricePSqft_list.append(PricePSqft[L_PricePSqft].text)

#   working well 25 May 2022 Wed 3:11PM


dList = list(zip(Listingprice_list, PricePSqft_list))
List = pd.DataFrame(dList, columns=['Listing Price', 'Listing Price Per SQFeet'])
List.to_csv('Test.csv', index=False)

#   Mission Complete
#   Working well as planned 26 May 2022 THU 12:28 AM
driver.quit()
print("END")
exit('')

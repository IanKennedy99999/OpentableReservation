import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

url = 'https://www.opentable.com/'
restaurant = 'villa-francesca'
partysize = 4

c = webdriver.ChromeOptions()
c.add_argument("--incognito")
c.add_argument(("--window-size=900,700"))
driver = webdriver.Chrome(options=c)
driver.get(url+restaurant)

time.sleep(1)
#element = driver.find_element(By.XPATH,'//*[@id="restProfileMainContentDtpPartySizePicker"]')
#element.click()
count = 0
while count != 1:
    try:
        dropdown = Select(driver.find_element(By.XPATH, '//*[@id="restProfileMainContentDtpPartySizePicker"]'))
        dropdown.select_by_index(partysize - 1)
        count+=1
        break
    except:
        print("failed party size with xpath 1")
        time.sleep(0.5)
        pass
    try:
        dropdown = Select(driver.find_element(By.XPATH, '//*[@id="overview-section"]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/select'))
        dropdown.select_by_index(partysize - 1)
        count += 1
        break
    except:
        print("failed party size with xpath 2")
        time.sleep(0.5)
        pass
    try:
        dropdown = Select(driver.find_element(By.ID,'restProfileMainContentDtpPartySizePicker'))
        dropdown.select_by_index(partysize - 1)
        count+=1
        break
    except:
        print('failed party size with ID')
        time.sleep(0.5)
        pass
    try:
        dropdown = Select(driver.find_element(By.NAME,'Party Size'))
        dropdown.select_by_index(partysize - 1)
        count+=1
        break
    except:
        print('failed party size with name')
        time.sleep(0.5)
        pass

time.sleep(1)
bount = 0
while bount != 1:
    try:
        dropdown = Select(driver.find_element(By.XPATH,'//*[@id="restProfileMainContenttimePickerDtpPicker"]'))
        dropdown.select_by_visible_text('8:00 PM')
        bount+=1
        break
    except:
        print('failed time with xpath 1')
        time.sleep(0.5)
        pass
    try:
        dropdown = Select(driver.find_element(By.XPATH, '//*[@id="overview-section"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/select'))
        dropdown.select_by_visible_text('8:00 PM')
        bount += 1
        break
    except:
        print('failed time with xpath 2')
        time.sleep(0.5)
        pass

    try:
        element = (driver.find_element(By.NAME, 'Time selector'))
        element.click()
        dropdown = Select(driver.find_element(By.NAME, 'Time selector'))
        dropdown.select_by_visible_text('8:00 PM')
        bount+=1
        break
    except:
        print('failed time with name')
        time.sleep(0.5)
        pass
try:
    element = driver.find_element(By.XPATH,'//*[@id="restProfileMainContentDtpDayPicker"]')
    element.click()
    time.sleep(1)
    element = driver.find_elements(By.NAME, "Wed, Feb 23, 2022]")
    element.click()
    print('success')
except:
    print('failed date with xpath 1')

try:
    element = driver.find_element(By.XPATH,'//*[@id="overview-section"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/button')
    element.click()
    time.sleep(1)
    element = driver.find_elements(By.NAME, "Wed, Feb 23, 2022]") #this is where the problem is I think
    element.click()
    print('success')
except:
    print('failed date with xpath 2')

#https://www.opentable.com/villa-francesca?corrid=bdf38ff4-7398-43a9-8b6a-2f898b30ea87&avt=eyJ2IjoyLCJtIjowLCJwIjowLCJzIjowLCJuIjowfQ&p=2&sd=2022-02-21T19%3A00%3A00
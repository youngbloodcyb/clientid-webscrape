from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# set driver as chrome and nav to Ampry admin portal
driver = webdriver.Chrome()
driver.get('https://{SITE}')

# create login variables
email = '{LOGIN EMAIL}'
password = '{PASSWORD}'

# sign in
username_field = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/app-log-in/div/div/div[2]/div[2]/input')
username_field.send_keys(email)

password_field = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/app-log-in/div/div/div[2]/div[3]/input')
password_field.send_keys(password)

login_button = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/app-log-in/div/div/div[2]/div[4]')
login_button.click()

driver.implicitly_wait(10)

# navigate to tenants page and set view per page to 50
tenants = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/app-admin-panel/div[2]/div[1]/div[3]/div')
tenants.click()

list_tenants = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/app-admin-panel/div[2]/div[1]/div[3]/div/div/div[1]/a')
list_tenants.click()

view_per_page = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/app-admin-panel/div[2]/div[2]/div/app-list-tenants/div/div/div[2]/div[3]/div[2]/div[1]/div[4]')
view_per_page.click()

# set xpath for each element
url_list = []
for i in range(1, 51):
    url_list.append('//*[@id="mainContainer"]/app-admin-panel/div[2]/div[2]/div/app-list-tenants/div/div/div[2]/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[10]/a')

# get href attribute of each element that includes the account id and add to list id_list
id_list = []
for s in url_list:
    account_id = driver.find_element(By.XPATH, s)
    id_list.append(account_id.get_attribute('href'))

# set xpath for name element
name_element_xpath_list = []
for n in range(1, 51):
    name_element_xpath_list.append('//*[@id="mainContainer"]/app-admin-panel/div[2]/div[2]/div/app-list-tenants/div/div/div[2]/div[3]/div[1]/table/tbody/tr[' + str(n) + ']/td[2]')

# get text values of each name html element and append to name_list
name_list = []
for x in name_element_xpath_list:
    name_list.append(driver.find_element(By.XPATH, x).text)

# print(id_list)
# print(name_list)

# give a few seconds to ensure lists propagate
time.sleep(3)
driver.implicitly_wait(10)

# click to next page of customers
next_element = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/app-admin-panel/div[2]/div[2]/div/app-list-tenants/div/div/div[2]/div[3]/div[2]/div[2]/pages/div/div/div[7]')

next_element.click()
time.sleep(3)
driver.implicitly_wait(10)

for a in name_element_xpath_list:
    name_list.append(driver.find_element(By.XPATH, a).text)


# # get href attribute of each element that includes the account id and add to list id_list
for c in url_list:
    account_id = driver.find_element(By.XPATH, c)
    id_list.append(account_id.get_attribute('href'))

# give a few seconds to ensure lists propagate
time.sleep(3)
driver.implicitly_wait(10)

### 3rd page

next_element.click()
time.sleep(3)
driver.implicitly_wait(10)

for d in name_element_xpath_list:
    name_list.append(driver.find_element(By.XPATH, d).text)


# # get href attribute of each element that includes the account id and add to list id_list
for e in url_list:
    account_id = driver.find_element(By.XPATH, e)
    id_list.append(account_id.get_attribute('href'))

# give a few seconds to ensure lists propagate
time.sleep(3)
driver.implicitly_wait(10)

### 4th page

next_element.click()
time.sleep(3)
driver.implicitly_wait(10)

for e in name_element_xpath_list:
    name_list.append(driver.find_element(By.XPATH, e).text)


# # get href attribute of each element that includes the account id and add to list id_list
for f in url_list:
    account_id = driver.find_element(By.XPATH, f)
    id_list.append(account_id.get_attribute('href'))

# give a few seconds to ensure lists propagate
time.sleep(3)
driver.implicitly_wait(10)

### 5th page

next_element.click()
time.sleep(3)
driver.implicitly_wait(10)

for g in name_element_xpath_list:
    name_list.append(driver.find_element(By.XPATH, g).text)


# # get href attribute of each element that includes the account id and add to list id_list
for h in url_list:
    account_id = driver.find_element(By.XPATH, h)
    id_list.append(account_id.get_attribute('href'))

# give a few seconds to ensure lists propagate
time.sleep(3)
driver.implicitly_wait(10)

### 6th page

next_element.click()
time.sleep(3)
driver.implicitly_wait(10)

last_page_name_list = []
for z in range(1, 17):
    last_page_name_list.append(('//*[@id="mainContainer"]/app-admin-panel/div[2]/div[2]/div/app-list-tenants/div/div/div[2]/div[3]/div[1]/table/tbody/tr[' + str(z) + ']/td[2]'))


for j in last_page_name_list:
    name_list.append(driver.find_element(By.XPATH, j).text)

last_page_url_list = []
for y in range(1, 17):
    last_page_url_list.append('//*[@id="mainContainer"]/app-admin-panel/div[2]/div[2]/div/app-list-tenants/div/div/div[2]/div[3]/div[1]/table/tbody/tr[' + str(y) + ']/td[10]/a')

# # get href attribute of each element that includes the account id and add to list id_list
for k in last_page_url_list:
    account_id = driver.find_element(By.XPATH, k)
    id_list.append(account_id.get_attribute('href'))

# give a few seconds to ensure lists propagate
time.sleep(3)
driver.implicitly_wait(10)

print(id_list)
print(name_list)

### turn lists into a dataframe
dict = {
    'client' : name_list,
    'id' : id_list
}

df = pd.DataFrame(dict)

df.to_csv('{FILEPATH}.csv', sep=',', header=True)

import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Selenium
chrome_driver_path = '/Users/matiyasmaru/Documents/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

form_link = 'https://docs.google.com/forms/d/1fvg6Q0vQClRiBcqDMmRLzdK0vuq07EzQuC2CeS8M0qA/viewform?edit_requested=true'
zillow_link = 'https://www.zillow.com/falls-church-va/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Falls%20Church%2C%20VA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-77.28738507495117%2C%22east%22%3A-77.05426892504883%2C%22south%22%3A38.79574866061918%2C%22north%22%3A38.96359098216598%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4679%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A547875%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2600%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
HEADERS = ({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25"','Accept-Language': 'en-US, en;q=0.5'})

response = requests.get(zillow_link, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find_all(class_='StyledPropertyCardDataWrapper-c11n-8-73-8__sc-1omp4c3-0 gXNuqr property-card-data')

links = ['https://www.zillow.com/' + (data[i].find(name='a').get('href')) for i in range(len(data))]
address = [data[i].find(name='a').text for i in range(len(data))]
price = [data[i].find(name='span').text.split('+')[0] for i in range(len(data))]


driver.get(form_link)
time.sleep(.5)
for i in range(len(links)):
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address[i])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price[i])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links[i])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    time.sleep(.5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


driver.quit()




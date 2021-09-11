import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def clear_input_box(driver):
	driver.find_element_by_xpath('//input[@autocapitalize]').clear()

def search_keyword(driver, Keyword):
	driver.find_element_by_xpath('//input[@autocapitalize]').send_keys(Keyword)

def get_result(driver):
	try:
		return driver.find_element_by_xpath('//span[text()=" posts"]/span').text
	except:
		return None


options = uc.ChromeOptions()
options.user_data_dir = "chrome_profile"
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)
driver.get('https://instagram.com')

input('Log in and press enter to continue... ')

keys = [i['keys'] for i in pd.read_csv('import.csv').to_dict('records')]

d = []
for key in keys:
	clear_input_box(driver)
	search_keyword(driver, key)
	time.sleep(5)
	result = get_result(driver)
	print(f"{key} - {result}")
	d.append({
		'keyword':key,
		'result':result
		})
pd.DataFrame(d).to_csv('export.csv')
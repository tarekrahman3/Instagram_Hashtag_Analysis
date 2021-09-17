import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from random import randint as rand

def clear_input_box(driver):
	driver.find_element_by_xpath('//input[@autocapitalize]').clear()

def search_keyword(driver, Keyword):
	driver.find_element_by_xpath('//input[@autocapitalize]').send_keys(Keyword)

def get_result(driver, key:str):
	post_number_xpath = f'//input[@autocapitalize]/following-sibling::div//div[text()="{key}" and text()="#"]/../../..//span[text()=" posts" or text()=" post"]/span'
	try:
		return driver.find_element_by_xpath(post_number_xpath).text
	except:
		return None

driver = uc.Chrome()
driver.get('https://www.instagram.com/accounts/login/')

input('Log in and press enter to continue... ')

keys = [i['keys'] for i in pd.read_csv('import.csv').to_dict('records')]

d = []
try:
	i=1
	for key in keys:
		clear_input_box(driver)
		search_keyword(driver, key)
		time.sleep(rand(5,7))
		result = get_result(driver, key)
		print(f"{i} - {key} - {result}")
		d.append({
			'time':time.ctime(),
			'keyword':key,
			'result':result
			})
		i+=1
finally:
	pd.DataFrame(d).to_csv('export.csv')

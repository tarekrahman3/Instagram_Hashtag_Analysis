import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def eval_posts(driver):
	try:
		driver.find_element_by_xpath('//header//span[text()=" posts" or text()=" post"]/span')
		return True
	except:
		return False

def eval_single_match(driver):
	try:
		driver.find_element_by_xpath('//h1')
		return True
	except:
		return False

def eval(driver):
	try:
		driver.find_element_by_xpath("""//*[text()="Sorry, this page isn't available."]""")
		return True
	except:
		return False



options = uc.ChromeOptions()
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)
keys = [i['keys'] for i in pd.read_csv('import.csv').to_dict('records')]
driver.get('https://instagram.com')

input('Log in and press enter to continue... ')
d = []
i=1
for key in keys:
	driver.get(f'https://www.instagram.com/explore/tags/{key}')
	time.sleep(6)
	if eval(driver)==True:
		result = 0
	elif eval_single_match(driver)==True & eval_posts(driver)==False:
		result = 1
	else:
		result = driver.find_element_by_xpath('//header//span[text()=" posts" or text()=" post"]/span').text
	print(f"{i} - {key} - {result}")
	d.append({
		'time':time.ctime(),
		'keyword':key,
		'result':result
		})
	i+=1
pd.DataFrame(d).to_csv('export.csv')


from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException


options = Options()
options.add_argument('--start-maximized')
PATH = './chromedriver.exe'
driver = webdriver.Chrome(PATH, options = options)

driver.get('https://www.quora.com/')

email = driver.find_element_by_xpath("//div[@class='form_column']/input[@name='email']")
email.send_keys('your_email')

password = driver.find_element_by_xpath("//div[@class='form_column'][2]/input[@name='password']")
password.send_keys('your_password')
password.send_keys(Keys.RETURN)


profile_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div[4]/div/div[1]/div/div/div/div/div/div/img")))
profile_icon.click()
partners = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div/div[2]/a[1]/div/div[2]/div/div")))
partners.click()

all_questions = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card_inner")))

i = 1
print(len(all_questions),'\n')
while i < len(all_questions) - 1:
	if i == 5:
		continue
	try:
		try:
			request_btn = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[5]/div/div/div/div/div[2]/div[7]/div/div/div[1]/div[{}]/div/div/div[3]/span/a/div/div/div'.format(i))))
			request_btn.click()
		except:
			pass
		print(i)

		i += 1
		try:
			no_of_requests = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div')))
			requests_sent = re.findall('\D+(\d+)/',no_of_requests.text)[0]
		except:
			no_of_requests = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div')))
			requests_sent = re.findall('\D+(\d+)/',no_of_requests.text)[0]
		writer_no = 2
		t = 0
		while t < 25-int(requests_sent):
			send_request = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div/div[{}]/div/div/div[3]/div/div/div/span/span'.format(writer_no))))
			send_request.click()
			t += 1
			writer_no += 1
		
		try:
			no_of_requests = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div')))
			print(re.findall('\D+(\d+)/',no_of_requests.text)[0])
		except:
			no_of_requests = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div')))
			print(re.findall('\D+(\d+)/',no_of_requests.text)[0])
		try:
			done = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/span/button')))
			done.click()
		except:
			done = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/span/button')))
			done.click()

	except TimeoutException:
		print('TimeoutException!')


driver.quit()

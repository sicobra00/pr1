import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


email = [
'ARRAY KOSONG',
'heirloomkop1@gmail.com',
'h.eirloomkop1@gmail.com',
'arifpradana315@gmail.com',
'a.rifpradana315@gmail.com',
'pojoj49479@galotv.com',
'progaming1945@gmail.com',
'xotic50775@logodez.com',
'gayivi5221@chimpad.com',
'bawot47138@logodez.com',
'gipamip142@galotv.com',
'cekesa7282@logodez.com',
'tasayo7430@logodez.com',
'jaxiva9071@logodez.com',
'kotome8634@logodez.com',
'nebitad522@galotv.com',
'sexos86308@aregods.com',
'kalem84222@logodez.com',
'milica2140@galotv.com',
'falapah365@logodez.com',
'nasofax570@aregods.com',
'rirof98990@galotv.com',
'xipiri2327@logodez.com',
'vatiyi4772@logodez.com',
'ridef20414@chimpad.com'
]
passw = 'arpra123123@'

while True:
	for i in range(1, len(email)):
		op = Options()
		op.binary_location('/selenium_chrome/chromedriver')
		op.add_argument('--no-sandbox')
		op.add_argument('--headless')
		op.add_experimental_option("excludeSwitches", ["enable-logging"])
		driver = webdriver.Chrome(options=op)
		driver.implicitly_wait(15)
		print('AKUN '+str(i)+' | START HEROKU')
		driver.get('https://heroku.com/login')
		emailform = driver.find_element(By.XPATH, '//*[@id="email"]')
		emailform.send_keys(email[i])
		time.sleep(3)
		passform = driver.find_element(By.XPATH, '//*[@id="password"]')
		passform.send_keys(passw)
		time.sleep(3)
		buttonlogin = driver.find_element(By.XPATH, '//*[@id="login"]/form/button')
		buttonlogin.click()
		print('AKUN '+str(i)+' | LOGIN....')
		time.sleep(5)
		buttonlater = driver.find_element(By.XPATH, '//*[@id="mfa-later"]/button')
		buttonlater.click()
		time.sleep(15)


		try:
			driver.get('https://dashboard.heroku.com/apps/minerbecak'+str(i)+'/settings')
			buttondelete = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[2]/div[2]/ul/li[8]/div/div[2]/p/span/button')
			buttondelete.click()
			time.sleep(3)
			confirmform = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/div[2]/div/div/input')
			confirmform.send_keys('minerbecak'+str(i))
			time.sleep(3)
			buttondelete2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/div[3]/button[2]')
			buttondelete2.click()
			time.sleep(7)
			print('AKUN '+str(i)+' | HAPUS APP')
		except:
			pass


		driver.get('https://dashboard.heroku.com/new?template=https://github.com/sicobra00/project1')
		time.sleep(15)
		appnameform = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[2]/div[2]/form/div/div[3]/div[2]/div/input')
		appnameform.send_keys('minerbecak'+str(i))
		time.sleep(3)
		buttondeploy = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[2]/div[2]/form/div/div[5]/button')
		buttondeploy.click()
		print('AKUN '+str(i)+' | MINING STARTED')
		time.sleep(20)
		driver.close()
		time.sleep(5)
		driver.quit()
		os.system('cls')
		time.sleep(5)

	


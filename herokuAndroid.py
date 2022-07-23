import time
from selenium import webdriver
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
		options = webdriver.ChromeOptions()
		options.add_argument("--headless")
		options.add_argument("--no-sandbox")
		options.add_experimental_option("excludeSwitches", ["enable-logging"])
		driver = webdriver.Chrome(options=options)
		driver.implicitly_wait(25)
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

		try:
			buttonlater = driver.find_element(By.XPATH, '//*[@id="mfa-later"]/button')
			buttonlater.click()
		except:
			print('AKUN '+str(i)+' | Error : ',sys.exc_info()[1])
			pass

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
			print('AKUN '+str(i)+' | Error : ',sys.exc_info()[1])
			pass


		try:
			driver.get('https://dashboard.heroku.com/new?template=https://github.com/sicobra00/project1')
			time.sleep(15)
			appnameform = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[2]/div[2]/form/div/div[3]/div[2]/div/input')
			appnameform.send_keys('minerbecak'+str(i))
			time.sleep(3)
			buttondeploy = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[2]/div[2]/form/div/div[5]/button')
			buttondeploy.click()
			print('AKUN '+str(i)+' | MINING STARTED')
			time.sleep(30)
		except:
			print('AKUN '+str(i)+' | Error : ',sys.exc_info()[1])
			pass
		driver.close()
		time.sleep(5)
		driver.quit()
		time.sleep(5)

	


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


email = [
'ARRAY KOSONG',
'pipihix195@chimpad.com',
'vecoda7174@chimpad.com',
'xiwaj21235@aregods.com',
'cebilag314@logodez.com',
'gegilaj781@chimpad.com',
'neted40692@galotv.com',
'wotava8139@logodez.com',
'mehobi6530@aregods.com',
'pipeti6839@aregods.com',
'xicoy31440@galotv.com',
'kiwij92649@logodez.com',
'radeji5959@logodez.com',
'fisoxa5850@aregods.com',
'femodol814@aregods.com',
'xodipa1800@aregods.com',
'lahel67387@galotv.com',
'ditip45979@aregods.com',
'tavav38801@chimpad.com',
'gahik70030@logodez.com',
'gabis59822@aregods.com'
]
passw = 'arpra123123@'
namaapp = 'minerbenak' #ganti tiap sesi

while True:
	for x in range (9, 12):
		for i in range(1, len(email)):
			try:
				options = webdriver.ChromeOptions()
				options.add_argument("--headless")
				options.add_argument("--no-sandbox")
				options.add_argument("--start-maximized")
				options.add_experimental_option("excludeSwitches", ["enable-logging"])
				driver = webdriver.Chrome(options=options)
				driver.implicitly_wait(60)
				print('AKUN '+str(i)+' | START HEROKU')
				driver.get('https://id.heroku.com/login')
				time.sleep(10)
				print(driver.title)
				try:
					buttonacc = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
					buttonacc.click()
					time.sleep(5)
				except:
					print('AKUN '+str(i)+' | NO COOKIE BUTTON !')
					pass
				emailform = driver.find_element(By.ID, 'email')
				emailform.send_keys(email[i])
				time.sleep(3)
				passform = driver.find_element(By.ID, 'password')
				passform.send_keys(passw)
				time.sleep(3)
				buttonlogin = driver.find_element(By.NAME, 'commit')
				buttonlogin.click()
				time.sleep(5)
			except:
				print('AKUN '+str(i)+' | LOGIN GAGAL')
				continue

			try:
				buttonlater = driver.find_element(By.ID, 'mfa-later')
				buttonlater.click()
			except:
				print('AKUN '+str(i)+' | INFO : NO LATER BUTTON !')
				pass

			time.sleep(15)
			print(driver.title)
			time.sleep(60)
			print(driver.title)


			try:
				driver.get('https://dashboard.heroku.com/apps/'+namaapp+str(i)+'/settings')
				buttondelete = driver.find_element(By.CLASS_NAME, 'delete-app')
				buttondelete.click()
				time.sleep(3)
				confirmform = driver.find_element(By.CLASS_NAME, 'hk-input')
				confirmform.send_keys(namaapp+str(i))
				time.sleep(3)
				buttondelete2 = driver.find_element(By.CLASS_NAME, 'hk-button--danger-primary')
				buttondelete2.click()
				time.sleep(7)
				print('AKUN '+str(i)+' | HAPUS APP')
			except:
				print(driver.title)
				print('AKUN '+str(i)+' | INFO : APP TIDAK ADA')
				pass



			try:
				driver.get('https://dashboard.heroku.com/new?template=https://github.com/sicobra00/pr'+str(x))
				time.sleep(15)
				appnameform = driver.find_element(By.CLASS_NAME, 'ember-text-field')
				appnameform.send_keys(namaapp+str(i))
				time.sleep(3)
				buttondeploy = driver.find_element(By.CLASS_NAME, 'deploy-button')
				buttondeploy.click()
				print('AKUN '+str(i)+' | MINING STARTED')
				time.sleep(30)
				os.system('clear')
			except:
				print(driver.title)
				print('AKUN '+str(i)+' | MINING GAGAL')

			driver.close()
			time.sleep(5)
			driver.quit()
			time.sleep(5)

	


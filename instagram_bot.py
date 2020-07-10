from selenium import webdriver
import time
import urllib.request
import os


class InstaBot:

	def __init__(self, username=None, password=None):
		

		self.username = ""#--username
		self.password = ""#--password
		self.login_url = "https://www.instagram.com/accounts/login/"
		self.driver = webdriver.Chrome("./chromedriver.exe")
		self.logged_in = False


	def login(self):
		self.driver.get(self.login_url)

		time.sleep(3)
		login_btn = self.driver.find_element_by_xpath('//button[@type=\"submit\"]') 
		
		username_input = self.driver.find_element_by_name('username')
		password_input = self.driver.find_element_by_name('password')

		username_input.send_keys(self.username)
		password_input.send_keys(self.password)
		

		login_btn.click()

	def chat(self):
		time.sleep(3)
		open_chat_tab = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div')
		open_chat_tab.click()
		time.sleep(5)
		try:
			not_now_notify = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
			not_now_notify.click()
		except:
			pass
		time.sleep(3)
		user_to_send = self.driver.find_element_by_partial_link_text('yuvam_jepgosome')
		user_to_send.click()
		message = "Hello Bro"
		message_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
		#for i in range(500):
		message_button.send_keys(message)
		send_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
		send_button.click()

	def inc_followers(self):
		time.sleep(5)
		self.driver.get('https://www.instagram.com/chrishemsworth')
		time.sleep(1)
		followers_window = self.driver.find_element_by_partial_link_text('followers')
		followers_window.click()
		time.sleep(4)
		follow_buttons = self.driver.find_elements_by_xpath("//button[text()='Follow']")
		for a in range(len(follow_buttons)):
			follow_buttons[a].click()
			
				
if __name__ == '__main__':
	bot = InstaBot()
	bot.login()
	bot.chat()
	bot.inc_followers()

	
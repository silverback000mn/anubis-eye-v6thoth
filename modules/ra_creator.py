from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

class AccountCreator:
    def __init__(self):
        self.proxy_list = self._load_proxies()
        self.current_proxy = None
        
    def create_account(self):
        self._rotate_proxy()
        driver = self._init_driver()
        
        try:
            driver.get("https://www.instagram.com/accounts/emailsignup/")
            time.sleep(random.uniform(1.5, 3.0))
            
            # Preenche formulário com dados gerados
            email = f"user{random.randint(1000,9999)}@tempmail.com"
            username = f"anubis_follower_{random.randint(100,999)}"
            
            driver.find_element(By.NAME, "emailOrPhone").send_keys(email)
            driver.find_element(By.NAME, "fullName").send_keys("Silverback Anubis")
            driver.find_element(By.NAME, "username").send_keys(username)
            driver.find_element(By.NAME, "password").send_keys("Anubis@2024")
            
            # Submissão
            driver.find_element(By.XPATH, '//button[text()="Sign up"]').click()
            
            return {"status": "success", "username": username, "proxy": self.current_proxy}
            
        except Exception as e:
            return {"status": "error", "message": str(e)}

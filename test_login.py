from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

#test class:
class TestLogin:
    def setup_method(self):
        #Setup: Opening browser and navigating to login page
        self.driver = webdriver.Chrome()
        self.driver.get("E:/Projects/Selenium Project/test_login.html")
        self.driver.maximize_window()
        time.sleep(2)

    def teardown_method(self):
        #Closing the browser after tests
        self.driver.quit()
    
    def test_valid_login(self):
        #Checking the valid login credentials  
        self.driver.find_element(By.ID, "username").send_keys("testuser")  
        self.driver.find_element(By.ID, "password").send_keys("testpass")  
        self.driver.find_element(By.ID, "login-btn").click()  
        time.sleep(2)

        #verifying login successful by checking dashboard
        assert "Dashboard" in self.driver.page_source

    def test_invalid_login(self):
        #if login credentials are invalid
        """Test Case: Verify login with incorrect credentials."""
        self.driver.find_element(By.ID, "username").send_keys("testuser")  
        self.driver.find_element(By.ID, "password").send_keys("wrongpass")  
        self.driver.find_element(By.ID, "login-btn").click()
        time.sleep(2)

        # Verify login failed message
        assert "Invalid username or password" in self.driver.page_source

if __name__ == "__main__":
    pytest.main()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Crea un'istanza di webdriver per Edge
driver = webdriver.Edge()
username = "username"
password = "password"

# login di instaram
driver.get("https://www.instagram.com/accounts/login/")
sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Consenti solo i cookie essenziali']"))).click()
sleep(2)
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Non ora']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Non ora']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/"+username+"/']"))).click()
sleep(2)

# vai ai following
sleep(2)
num = driver.find_elements(By.XPATH,"//span[contains(@class, '_ac2a')]")

# vai ai follower
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/"+username+"/followers/']"))).click()
sleep(2)
follower_list = []
count = 0
while True:
    try:
        elements = driver.find_elements(By.XPATH,"//span/div")
        for element in elements:
            count += 1
            friend_username = element.text
            if "Italiano" not in friend_username and friend_username not in follower_list:
                follower_list.append(friend_username)
        driver.execute_script("arguments[0].scrollIntoView(true);", elements[-1])
        sleep(2)
        if count > int(num[1].text):
            break
    except NoSuchElementException:
        continue
driver.find_elements(By.XPATH, "//button[contains(@class, '_abl-')]")[1].click()
print("follower_list")
print(follower_list)

# vai ai following e smette di seguire chi non ti segue
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/"+username+"/following/']"))).click()
sleep(2)
count = 0
while True:
    try:
        elements = driver.find_elements(By.XPATH,"//div[contains(@class,'x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x6s0dn4 xozqiw3 x1q0g3np')]")
        for element in elements:
            count += 1
            friend_username = element.find_element(By.XPATH,".//span/div").text
            if "Italiano" not in friend_username and friend_username not in follower_list:
                element.find_element(By.XPATH,".//button[contains(@class, '_acan')]").click()
                driver.find_element(By.XPATH,"//button[text()='Non seguire più']").click()
                sleep(2)
        driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_elements(By.XPATH,"//span/div")[-1])
        sleep(2)
        if count > int(num[2].text):
            break
    except NoSuchElementException:
        continue
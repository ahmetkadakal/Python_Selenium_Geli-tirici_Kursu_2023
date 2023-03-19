from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())



class Tasks:
    def __init__(self):
        pass

    def goToTheSite():
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        driver.maximize_window()
        sleep(5)
        print("GİRİŞ BAŞARILI")
    def fullEmpty():
        driver.find_element(By.ID,"login-button").click()
        sleep(5)
        print("FULL BOŞ TESTİ BAŞARILI")
    def justPassword():
        driver.find_element(By.NAME,"user-name").send_keys("standard_user")
        sleep(1)
        driver.find_element(By.ID,"login-button").click()
        sleep(5)
        print("ŞİFRESİZ GİRİŞ TESTİ BAŞARILI")
    def lockedOutUser():
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.NAME,"user-name").send_keys("locked_out_user")
        sleep(1)
        driver.find_element(By.NAME,"password").send_keys("secret_sauce")
        sleep(1)
        driver.find_element(By.ID,"login-button").click()
        sleep(5)
        print("KİLİTLİ KULLANICI TESTİ BAŞARILI")
    def warningClose():
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        driver.find_element(By.ID,"login-button").click()
        sleep(5)
        driver.find_element(By.CLASS_NAME,"error-button").click()
        sleep(5)
        print("UYARI KAPATMA TESTİ BAŞARILI")
    def login():
        driver.find_element(By.NAME,"user-name").send_keys("standard_user")
        driver.find_element(By.NAME,"password").send_keys("secret_sauce")
        sleep(1)
        driver.find_element(By.ID,"login-button").click()
        print("Siteye giriş sağlandı")
        listOfproducts = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Ürün sayısı {len(listOfproducts)} ")
        sleep(2)
        driver.close()
        
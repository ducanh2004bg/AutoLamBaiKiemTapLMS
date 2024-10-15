# -*- coding: utf-8 -*-
import time
import os

# Kiểm tra và cài đặt các thư viện cần thiết nếu chưa có
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from colorama import Fore, Back, Style, init
    import pyautogui
    import random
    import getpass

except ImportError:
    os.system("pip install seleniumbase")
    os.system("pip install selenium")
    os.system("pip install pyautogui")
    os.system("pip install colorama")
    from colorama import Fore, Back, Style, init
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    import pyautogui
    import random
    import getpass


from time import sleep

print(f"{Fore.RED} LMSHelper Bảo Trì Hôm Nay!!!"

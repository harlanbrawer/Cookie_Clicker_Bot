#selenium is the web driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#initialize web driver with browser and website
driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/cookieclicker/")

#give time to load
time.sleep(5)

#select the element to be clicked
cookie = driver.find_element_by_id("bigCookie")

#array of upgrades to be clicked on
product_names = ["product0", "product1", "product2", "product3",
	"product4", "product5", "product6", "product7", "product8", 
	"product9", "product10", "product11", "product12", "product13", 
	"product14", "product15"]

#upgrade driver array
products = []

#configure driver for each upgrade to be clicked
for product_name in product_names:
		products.append(driver.find_element_by_id(product_name))

#function that attempts to purchase each upgrade starting from cheapest
def upgrade():
	for product in products:
		product.click()

#click loop
i = 0
while True:
	try:
		i += 1
		driver.execute_script("arguments[0].click();", cookie)
	except:
		i += 1
		continue
	if i > 100:
		try:
			#try to upgrade every 100 ticks
			i = 0
			upgrade()
		except:
			i = 0
			continue
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/cookieclicker/")

time.sleep(5)
cookie = driver.find_element_by_id("bigCookie")

product_names = ["product0", "product1", "product2", "product3",
	"product4", "product5", "product6", "product7", "product8", 
	"product9", "product10", "product11", "product12", "product13", 
	"product14", "product15"]

products = []

for product_name in product_names:
		products.append(driver.find_element_by_id(product_name))

def upgrade():
	for product in products:
		product.click()

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
			i = 0
			upgrade()
		except:
			i = 0
			continue
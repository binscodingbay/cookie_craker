from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

'''first approach where we target individual elements in a systematic order and find the maximum affordable upgrade
according to our current cookie count '''
# items_list=[]
# id_list=[]
# cookie = driver.find_element(By.ID, "cookie")
# # for i in range(100):
# #     cookie.click()
#
#
# #get the ids of the upgrades
# find_ids = driver.find_elements(By.CSS_SELECTOR, "#store div")
# for item in find_ids:
#     if len(item.get_attribute("ID"))!=0:
#         id_list.append(item.get_attribute("ID"))
#
# print(id_list)
# time_to_check_upgrades = time.time()+5
five_min = time.time() + 60*5 # 5minutes
# while True:
#     cookie.click()
#
#     if time.time()>time_to_check_upgrades:
#         # Get all upgrade <b> tags
#         all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
#         item_prices = []
#
#         # Convert text into an integer price.
#         for price in all_prices:
#             element_text = price.text
#             print(element_text)
#             if len(element_text) != 0:
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)
#
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = id_list[n]
#
#         # Get current cookie count
#         money_element = driver.find_element(By.ID, "money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)
#
#         # Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#
#
#
#         # Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#         driver.find_element(By.ID, to_purchase_id).click()
#
#         # Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#         # After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element(By.ID, "cps").text
#         print(cookie_per_s)
#         break
#
#         # money = int(driver.find_element(By.ID, "money").text)
#
#
# #     # time.sleep(10)
# #     BuyCursor = driver.find_element(By.ID, "buyCursor")
# #     BuyCursor.click()
#
#
# time.sleep(60)
# driver.quit()

'''this second approach allows us to achieve maximum cookies per second in 5 mins by using
a random fashion of clicking on upgrades 83.8'''
def clicking():
    # Target all store elements
    upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")
    for i in range(len(upgrades), -1, -1):
        try:
            upgrades[i].click()
        except:
            continue

bigcookie = driver.find_element(By.ID, "cookie")

while True:
    # Click 100 times per second for 5 seconds
    for i in range(0, 500):
        bigcookie.click()

    # After 5 seconds click every item in the store in reverse 5 times
    # This helps in the early game where you can often do multiple upgrades per 5 second increment
    for i in range(0, 5):
        clicking()
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
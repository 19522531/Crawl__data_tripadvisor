from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = "https://www.tripadvisor.com.vn/Restaurants-g293925-Ho_Chi_Minh_City.html"
link2 = "https://www.tripadvisor.com.vn/RestaurantSearch-g293925-oa30-zfp10600-Ho_Chi_Minh_City.html#EATERY_LIST_CONTENTS"
driver.get(link)

list_link = []
count = 30
for i in range(30):
    if i ==0:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(link)
        time.sleep(3)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        link3 = link2.replace("oa30", "oa"+str(count*i))
        driver.get(link3)
        time.sleep(3)
        links = driver.find_elements_by_class_name("bHGqj")
        time.sleep(10)
        for lk in links:
            href  = lk.get_attribute("href")
            if href not in list_link:
                list_link.append(href) 
    driver.close()
        
    

text = "\n".join(list_link)
with open("list_link.txt", "w", encoding="utf8") as file:
    file.write(text)

print(len(list_link))

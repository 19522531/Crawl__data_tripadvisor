from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = "https://www.tripadvisor.com/Restaurants-g293925-Ho_Chi_Minh_City.html"
driver.get(link)

list_link = []
links = driver.find_elements_by_class_name("bHGqj")
# for i in links:
#     print(i.get_attribute("href"))
for i in range(10):
    links = driver.find_elements_by_class_name("bHGqj")
    for i in links:
        link = i.get_attribute("href")
        if link not in list_link:
            list_link.append(link)
    time.sleep(3)
    btn_next = driver.find_element_by_class_name("rndBtn")
    btn_next.click()
    time.sleep(3)
   
    
    
text = "\n".join(list_link)
with open("list_link.txt", "w", encoding="utf8") as file:
    file.write(text)

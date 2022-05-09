from ast import Constant
from xml.dom.minidom import Element
from click import option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC 
import time
from datetime import datetime

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

sleep_long = 30
sleep_short = 10
def preprocessing(text):
    text = text.replace("\n", ".")
    text = text.replace("..", ".")
    text = text.replace("...", ".")
    text = text.replace(". .", ".")
    text = " ".join(text.split())
    return text
def get_list_comments_by_link(link):


    count = 0
    lst = []
    Flag= True
    link2 = link
    while Flag==True:
        print(link2)
        print(count)
        print(len(lst))
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(link2)

        try:
            btn_showmore = driver.find_element_by_class_name("ulBlueLinks")
            time.sleep(sleep_long)
            btn_showmore.click()
        except:
            print("lỗi")
            Flag = False
            continue

        time.sleep(sleep_short)
        list_comment = driver.find_elements_by_class_name("partial_entry")
        time.sleep(30)
        if len(list_comment) == 0:
            return
        for comment in list_comment:
            comt = preprocessing(comment.text)
            if comt in lst:
                Flag= False
                break
            if ("Thân gửi" not in comt) and ("Thanks for" not in comt):       
                lst.append(comt)   
                
            
            
        driver.close()
        time.sleep(3)
        count+=10
        link2  = link.replace("Reviews", "Reviews"+"-or"+str(count))

        
    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")
    with open("./Data/" + current_time+ ".txt", "w", encoding="utf8") as file:
        file.write("\n\n".join(lst))
    

def extra_comment(path):
    with open(path , "r", encoding="utf8") as file:
        list_link = file.read().split("\n")
    for link in list_link[:50]:
        try:
            get_list_comments_by_link(link)
        except:
            print("không có vietnamese")
            continue
# path = "list_link.txt"
# extra_comment(path)

path = "list_link.txt"
extra_comment(path)


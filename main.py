from ast import Constant
from xml.dom.minidom import Element
from click import option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC 
import time
from datetime import datetime

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

sleep_long = 30
sleep_short = 10
def get_list_comments_by_link(link):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(link)
    
    time.sleep(sleep_long)    

    ### button language click
    check_lang =  btn = driver.find_elements_by_xpath("//span[contains(text(), 'More languages')]")
    time.sleep(sleep_short)
    check_lang[0].click()
    
    ###  button vietnamese click to select vietnamese
    try:
        btn_vi = driver.find_element_by_id("filters_detail_language_filterLang_vi")
        time.sleep(sleep_long)
        btn_vi.click()
        time.sleep(sleep_short)
    except:
        print("No Vietnamese")
        driver.close()
        return
    


    btn_showmore = driver.find_element_by_class_name("ulBlueLinks")
    time.sleep(sleep_long)
    btn_showmore.click()

    time.sleep(sleep_short)
    list_comment = driver.find_elements_by_class_name("partial_entry")
    lst = []
    for comment in list_comment:
        comt = comment.text
        if "Dear" not in comt :       
            lst.append(" ".join(comt.split()))
    now = datetime.now()

    current_time = now.strftime("%H_%M_%S")
    with open("./Data/" + current_time+ ".txt", "w", encoding="utf8") as file:
        file.write("\n\n".join(lst))
    driver.close()

def extra_comment(path):
    with open(path , "r", encoding="utf8") as file:
        list_link = file.read().split("\n")
    for link in list_link:
        try:
            get_list_comments_by_link(link)
        except:
            continue
path = "list_link.txt"
extra_comment(path)
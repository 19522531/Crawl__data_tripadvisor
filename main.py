from xml.dom.minidom import Element
from click import option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC 
import time
from datetime import datetime

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



def get_list_comments_by_link(link):
    driver.get(link)
    
    time.sleep(5)    

    ### button language click
    check_lang =  btn = driver.find_elements_by_xpath("//span[contains(text(), 'More languages')]")
    check_lang[0].click()
    time.sleep(10)
    
    ###  button vietnamese click to select vietnamese
    try:
        btn_vi = driver.find_element_by_id("filters_detail_language_filterLang_vi")
        # btn_vi = driver.find_element_by_xpath("//span[contrains(text(),'Vietnamese')]")
        # time.wait(3)
        time.sleep(30)
        btn_vi.click()
        time.sleep(3)
    except:
        print("No Vietnamese")
        driver.close()
        driver.quit()
        return
    


    time.sleep(5)

    btn_showmore = driver.find_element_by_class_name("ulBlueLinks")
    time.sleep(20)
    btn_showmore.click()

    time.sleep(3)
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
    driver.quit()

    # next_btn = driver.find_elements_by_xpath("//a[contains(text(), 'Next')]")
    # if len(next_btn)>=2:
    #     link  = next_btn[0].get_attribute("href")
    #     print("replace link\n\n")
    #     print(link)
    # else: 
    #     print("Not replace\n\n")  

# with open("list_link.txt" , "r", encoding="utf8") as file:
#     list_link = file.read().split("\n")
# for link in list_link:
#     try:
#         get_list_comments_by_link(link)
#     except:
#         continue
link = "https://www.tripadvisor.com//Restaurant_Review-g293925-d5565387-Reviews-Hard_Rock_Cafe-Ho_Chi_Minh_City.html"
get_list_comments_by_link(link)
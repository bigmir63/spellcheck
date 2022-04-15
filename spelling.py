from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import time

fp = open("1.txt",'r')
# fp = open("1.txt",'r', encoding= "utf-8")

text = fp.read()
fp.close()


ready_list = []
while (len(text) >500 ):
    temp_str = text[:500]
    last_space = temp_str.rfind(' ')
    temp_str = text[0:last_space]
    ready_list.append(temp_str)
    text = text[last_space:]

ready_list.append(text)


dv = webdriver.Chrome()

dv.get("http://www.naver.com")

elem = dv.find_element_by_name("query")

elem.send_keys("맞춤법 검사기")
elem.send_keys(Keys.RETURN)

textarea = dv.find_element_by_class_name("txt_gray")


new_str = ''

for ready in ready_list:

    textarea.send_keys(Keys.CONTROL,"a") 
    textarea.send_keys(ready)
    elem = dv.find_element_by_class_name("btn_check")
    elem.click()
    time.sleep(1)
    soup = BeautifulSoup(dv.page_source,'html.parser')
    st = soup.select("p._result_text.stand_txt")[0].text
    new_str += st.replace('. ', '.\n')

fp = open("result.txt", 'w')
fp.write(new_str)
fp.close 

# elem.send_keys("안녕하세오 반가숩니다.")
# elem = dv.find_element_by_class_name("btn_check")
# elem.click()

# soup = BeautifulSoup(dv.page_source,'html.parser')

# print(soup.prettify())

# print (soup.select("p._result_text.stant_txt")[0].text)

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
import time 
import pyautogui 
import win32api 
from win32con import * 
import requests 
from bs4 import BeautifulSoup 
import json

service = Service() options = webdriver.ChromeOptions() driver = webdriver.Chrome(service=service, options=options) #driver.get('https://2gis.kz/almaty/firm/9429940001624593/tab/inside/filters/rubric_id%3D110579?m=76.928687%2C43.263743%2F16') mega park #driver.get('https://2gis.kz/almaty/firm/9429940000979694/tab/inside?m=76.927826%2C43.218628%2F16') esentai driver.get('https://2gis.kz/almaty/firm/70000001079903375/tab/inside?m=77.024042%2C43.314913%2F16')

time.sleep(1)

temp = driver.find_element('xpath', '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div[3]/h2/a/span')
store_count = int(temp.text)

def shoe(): 
    index = 1 
    skip = 0 
    time.sleep(1) 
    while True: 
        try: 
            driver.find_element('xpath', '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[40]/div/button') 
            time.sleep(0.5) 
            break 
        except: 
            try: 
                driver.find_elements(By.CLASS_NAME, '_zjunba')[index - 1].click() 
                time.sleep(0.5)
                # name
                store_name_class = driver.find_element(By.CLASS_NAME, '_tvxwjf')
                store_name_span = store_name_class.find_element(By.TAG_NAME, 'span')
                store_name = store_name_span.text

                # category
                store_category_class = driver.find_element(By.CLASS_NAME, '_1tfwnxl')
                store_category_span = store_category_class.find_element(By.CLASS_NAME, '_1w9o2igt')
                store_category = store_category_span.text

                # working time
                try:
                    store_working_time_class = driver.find_elements(By.CLASS_NAME, '_172gbf8')[1].find_element(By.CLASS_NAME, '_18zamfw')
                    store_working_time = store_working_time_class.text
                except:
                    store_working_time_class = driver.find_elements(By.CLASS_NAME, '_172gbf8')
                    store_working_time = ""

                    for i in store_working_time_class:
                        temp = WebDriverWait(driver, 0.2).until(
                            EC.presence_of_element_located((By.CLASS_NAME, '_18zamfw'))
                        )

                        if temp:
                            store_working_time = i.text
                            break

                # phone numbers
                try:
                    store_phone_number_button = driver.find_element(By.CLASS_NAME, '_1ns0i7c')
                    store_phone_number_button.click() # нажали на показать телефон
                    time.sleep(0.1)
                    store_phone_number_class = driver.find_elements(By.CLASS_NAME, '_b0ke8')
                    store_phone_number = ""

                    for i in store_phone_number_class:    
                        store_phone_number += " " + i.text
                except:
                    store_phone_number = "-"

                # web-site
                store_link = ""
                try:
                    elem_site = driver.find_elements(By.XPATH, '//a[@class="_1rehek" and @target="_blank"]')
                    for i in elem_site:
                        if '.' in i.text:
                            store_link += " " + i.text

                    if store_link == "":
                        store_link = "-"
                except:
                    store_link = "-"
                    
                # social media
                try:
                    elem_social = driver.find_element(By.CLASS_NAME, '_2fgdxvm')
                    social_plus = elem_social.find_elements(By.TAG_NAME, 'a')
                    store_social_media = ""

                    for i in social_plus:
                        store_social_media += " " + i.get_attribute('aria-label') + ":" + " " + i.get_attribute('href')
                except:
                    store_social_media = "-"

                # photo
                try:
                    store_photo_class = driver.find_element(By.CLASS_NAME, '_5nvdrf').find_element(By.CLASS_NAME, '_1dk5lq4')
                    store_photo = store_photo_class.get_attribute('style').split('url(')[1]
                except:
                    store_photo = "-"

                # id
                store_id_class = driver.find_elements(By.CLASS_NAME, '_zjunba')
                store_id_tag = store_id_class[index - 1 - skip].find_element(By.TAG_NAME, 'a')
                store_id = store_id_tag.get_attribute('href')

                shoe_info.append({'Id': store_id, 'Name': store_name, 'Category': store_category, 'Time': store_working_time, 'Phone number': store_phone_number, 'Web-site': store_link, 'Photo': store_photo, 'Social media': store_social_media})

                if store_name == 'First Steps Orthopedic':
                    break
                    driver.close()

                driver.find_element('xpath', f'//*[@id="root"]/div/div/div[1]/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[{index}]/div/div[1]/a/span/span').click()
                time.sleep(0.2)
                win32api.mouse_event(MOUSEEVENTF_WHEEL, 100, 500, -200, 0)
                time.sleep(0.2)
                index += 1
            except:
                index += 1
                skip += 1
    
    def clothes(): 
        index = 1 
        skip = 0 
        while True: 
            try: 
                driver.find_element('xpath', '//[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[40]/div/button') 
        #driver 
                time.sleep(0.5) 
                break 
            except: 
                try: 
                    driver.find_element('xpath', f'//[@id="root"]/div/div/div[1]/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[{index}]/div/div[1]/a/span/span').click() 
                    time.sleep(0.2) 
                    count_for_end = driver.find_elements(By.CLASS_NAME, '_awwm2v') 
                    end = 0
                for i in count_for_end:
                    if 'Добавить организацию' in i.text:
                        end = driver.find_elements(By.CLASS_NAME, '_zjunba')

                # name
                store_name_class = driver.find_element(By.CLASS_NAME, '_tvxwjf')
                store_name_span = store_name_class.find_element(By.TAG_NAME, 'span')
                store_name = store_name_span.text

                # category
                store_category_class = driver.find_element(By.CLASS_NAME, '_1tfwnxl')
                store_category_span = store_category_class.find_element(By.CLASS_NAME, '_1w9o2igt')
                store_category = store_category_span.text

                # working time
                try:
                    store_working_time_class = driver.find_elements(By.CLASS_NAME, '_172gbf8')[1].find_element(By.CLASS_NAME, '_18zamfw')
                    store_working_time = store_working_time_class.text
                except:
                    store_working_time_class = driver.find_elements(By.CLASS_NAME, '_172gbf8')
                    store_working_time = ""

                    for i in store_working_time_class:
                        temp = WebDriverWait(driver, 0.2).until(
                            EC.presence_of_element_located((By.CLASS_NAME, '_18zamfw'))
                        )

                        if temp:
                            store_working_time = i.text
                            break

            # phone numbers
                try:
                    store_phone_number_button = driver.find_element(By.CLASS_NAME, '_1ns0i7c')
                    store_phone_number_button.click() # нажали на показать телефон
                    time.sleep(0.1)
                    store_phone_number_class = driver.find_elements(By.CLASS_NAME, '_b0ke8')
                    store_phone_number = ""

                    for i in store_phone_number_class:    
                        store_phone_number += " " + i.text
                except:
                    store_phone_number = "-"

                # web-site
                store_link = ""
                try:
                    elem_site = driver.find_elements(By.XPATH, '//a[@class="_1rehek" and @target="_blank"]')
                    for i in elem_site:
                        if '.' in i.text:
                            store_link += ", " + i.text

                    if store_link == "":
                        store_link = "-"
                except:
                    store_link = "-"
                    
                # social media
                try:
                    elem_social = driver.find_element(By.CLASS_NAME, '_2fgdxvm')
                    social_plus = elem_social.find_elements(By.TAG_NAME, 'a')
                    store_social_media = ""

                    for i in social_plus:
                        store_social_media += " " + i.get_attribute('aria-label') + ":" + " " + i.get_attribute('href')
                except:
                    store_social_media = "-"

                # photo
                try:
                    store_photo_class = driver.find_element(By.CLASS_NAME, '_5nvdrf').find_element(By.CLASS_NAME, '_1dk5lq4')
                    store_photo = store_photo_class.get_attribute('style').split('url(')[1]
                except:
                    store_photo = "-"

                # id
                store_id_class = driver.find_elements(By.CLASS_NAME, '_zjunba')
                store_id_tag = store_id_class[index - 1 - skip].find_element(By.TAG_NAME, 'a')
                store_id = store_id_tag.get_attribute('href')

                # formatting
                formatted_id = store_id.split('/')[-1]
                formatted_link = store_link
                formatted_photo = store_photo

                if store_link[0] != '-':
                    formatted_link = store_link[2:]

                if store_photo != '-':
                    formatted_photo = store_photo.split('"')[1]

                stores_info.append({'Id': formatted_id, 'Name': store_name, 'Category': store_category, 'Time': store_working_time, 'Phone number': store_phone_number, 'Web-site': formatted_link, 'Photo': formatted_photo, 'Social media': store_social_media})

                if store_name == 'Duetfur':
                    driver.get('https://2gis.kz/almaty/firm/70000001079903375/tab/inside?m=77.024042%2C43.314913%2F16')
                    time.sleep(0.1)
                    shoes_class = driver.find_elements(By.CLASS_NAME, '_lt317')

                    for i in shoes_class:
                        if i.text == 'Обувь':
                            i.click()
                    
                    shoe()
                    break
                
                driver.find_element('xpath', f'//*[@id="root"]/div/div/div[1]/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[{index}]/div/div[1]/a/span/span').click()
                time.sleep(0.2)
                win32api.mouse_event(MOUSEEVENTF_WHEEL, 100, 500, -200, 0)
                time.sleep(0.2)
                index += 1
            except:
                index += 1
                skip += 1
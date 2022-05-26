'''
만들고 싶은 기능
(3) 아이콘 넣기
(4) 창 이쁘기
(5) 하나의 프로그램으로 구워내기
'''

# to do list
# 6. 매일 실행되도록 프로그래밍
from msilib.schema import Class

import re
from selenium.webdriver.chrome.options import Options
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import datetime
import pandas as pd
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser



class crawling_corporation:
    def __init__(self) -> None:
        pass

    # 첫 단계
    def step1(self, corporation, driver, num, week, dates):
        # 진입
        if num == 0:
            sleep(3)
            driver.find_element_by_xpath('/html/body/div[2]/section[2]/aside/div[4]/ul/li[1]/ul/li[2]/div/div[1]/ul/li[2]/ul/li[3]/a').send_keys(Keys.ENTER)
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/section[2]/aside/div[4]/ul/li[1]/ul/li[2]/div/div[1]/ul/li[2]/ul/li[3]/ul/li[2]/a').send_keys(Keys.ENTER)
        # ----- 거래내역 뽑기 -----
        # 검색창 입력
        if num == 0:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[1]/div/table/tbody/tr[2]/td/div/div/p/img'))).click()
            search_cor = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/div[7]/div[2]/div/form/div[2]/input[1]')))
            search_cor.clear()
            search_cor.send_keys(corporation)
            search_cor.send_keys(Keys.RETURN)
            sleep(3)
            driver.find_element_by_xpath('/html/body/div[2]/section[2]/section/section/div/div[2]/div[7]/div[2]/div/form/div[2]/a').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/div[7]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]'))).click()
        sleep(2)
        # 날짜 입력
        end = driver.find_element_by_xpath('/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[1]/div/table/tbody/tr[3]/td[1]/div/div/input[2]')
        end.clear()
        end.send_keys(dates)
        sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[1]/div/table/tbody/tr[3]/td[1]/div/div/button[2]'))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[1]/div/a'))).click()
        sleep(4)
        html = driver.page_source
        # pip install lxml
        soup = BeautifulSoup(html, 'html.parser')
        table_html = soup.find('table', {'class' : 'CI-GRID-BODY-TABLE'})
        table_html = str(table_html)
        table_df_list = pd.read_html(table_html)
        table_df = table_df_list[0]
        Count = str(table_df['매수'][12])
        Corpor_count = str(table_df['순매수'][7])
        Personal_count = str(table_df['순매수'][9])
        Foreign_count = str(table_df['순매수'][10])
        # fin
        dic = {
            'Date': dates,
            'Count': Count,
            'Corpor_count': Corpor_count, 
            'Personal_count': Personal_count, 
            'Foreign_count': Foreign_count,
            'week': str(week)
        }
        return dic

    # 두번째 단계
    def step2(self, corporation, driver, num, week, dates):
        if num == 0:
            sleep(4)
            driver.find_element_by_xpath('/html/body/div[2]/section[2]/aside/div[4]/ul/li[1]/ul/li[2]/div/div[1]/ul/li[2]/ul/li[5]/a').send_keys(Keys.ENTER)
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/section[2]/aside/div[4]/ul/li[1]/ul/li[2]/div/div[1]/ul/li[2]/ul/li[5]/ul/li[2]/a').send_keys(Keys.ENTER)
            sleep(2)
            driver.find_element_by_xpath('//*[@id="MDCSTAT035_FORM"]/div[2]/div/table/tbody/tr[1]/td/label[2]').click()
        # 검색창 입력
        if num == 0:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[2]/div/table/tbody/tr[4]/td/div/div/p/img'))).click()
            search_cor = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/div[4]/div[2]/div/form/div[2]/input[1]')))
            search_cor.clear()
            search_cor.send_keys(corporation)
            search_cor.send_keys(Keys.RETURN)
            sleep(3)
            driver.find_element_by_xpath('/html/body/div[2]/section[2]/section/section/div/div[2]/div[4]/div[2]/div/form/div[2]/a').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]'))).click()
        sleep(2)
        # 날짜 입력
        end = driver.find_element_by_xpath('//*[@id="endCalendar"]')
        end.clear()
        end.send_keys(dates)
        sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[2]/div/table/tbody/tr[5]/td/div/div/button[2]'))).click()
        driver.find_element_by_xpath('/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[2]/div/a').click()
        sleep(4)
        per_html = driver.page_source
        soup = BeautifulSoup(per_html, 'html.parser')
        table_html = soup.find_all('table', {'class' : 'CI-GRID-BODY-TABLE'})
        table_html = str(table_html)
        table_df_list = pd.read_html(table_html)
        table_df = table_df_list[1]
        PER = str(table_df['PER'][0])
        PBR = str(table_df['PBR'][0])
        Price = str(table_df['종가'][0]) 
        #fin
        dic = {
            'Date': dates,
            'Price': Price,
            'PER': PER, 
            'PBR': PBR, 
        }       
        return dic
    
    # 세번째 단계
    def step3(self, corporation, driver, num, week, dates):
        if num == 0:
            sleep(4)
            driver.find_element_by_xpath('/html/body/div[2]/section[2]/aside/div[4]/ul/li[1]/ul/li[2]/div/div[1]/ul/li[2]/ul/li[5]/a').send_keys(Keys.ENTER)
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/section[2]/aside/div[4]/ul/li[1]/ul/li[2]/div/div[1]/ul/li[2]/ul/li[5]/ul/li[4]/a').send_keys(Keys.ENTER)
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[2]/div/table/tbody/tr[1]/td/label[2]').click()
        # 검색창 입력
        if num == 0:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[2]/div/table/tbody/tr[4]/td/div/div/p/img'))).click()
            search_cor = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/div[4]/div[2]/div/form/div[2]/input[1]')))
            search_cor.clear()
            search_cor.send_keys(corporation)
            search_cor.send_keys(Keys.RETURN)
            sleep(3)
            driver.find_element_by_xpath('/html/body/div[2]/section[2]/section/section/div/div[2]/div[4]/div[2]/div/form/div[2]/a').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]'))).click()
        sleep(2)
        # 날짜 입력
        end = driver.find_element_by_xpath('//*[@id="endCalendar"]')
        end.clear()
        end.send_keys(dates)
        sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[2]/div/table/tbody/tr[5]/td/div/div/button[2]'))).click()
        driver.find_element_by_xpath('/html/body/div[2]/section[2]/section/section/div/div[2]/form/div[2]/div/a').click()
        sleep(4)
        # 페이지 크롤링
        foreign_html = driver.page_source
        soup = BeautifulSoup(foreign_html, 'html.parser')
        table_html = soup.find_all('table', {'class' : 'CI-GRID-BODY-TABLE'})
        table_html = str(table_html)
        table_df_list = pd.read_html(table_html)
        table_df = table_df_list[1]
        Foreign_rate = str(table_df['외국인지분율'][0])
        # fin
        dic = {
            'Date': dates,
            'Foreign_rate': Foreign_rate,
        }
        return dic
    
    def summary():
        return 0




#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------



import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from selenium.webdriver.chrome.options import Options
import selenium
from selenium import webdriver
from time import sleep
from datetime import datetime, timedelta, date
import pandas as pd
import os


# 절대 경로
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(relative_path)))
    return os.path.join(base_path, relative_path)

form_1 = resource_path('1.ui')
form_2 = resource_path('2.ui')
chrom_exe = resource_path('chromedriver.exe')
print(form_1)
print(chrom_exe)
# UI파일 연결
form_class = uic.loadUiType(form_1)[0]
form_class_2 = uic.loadUiType(form_2)[0]



# 갑자기 안될 때는 크롬 버전이 달라서 그런 것이므로, 그에 맞는 driver 다운로드하면 된다.
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("start-maximized")
options.add_argument("--disable-software-rasterizer")
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")



#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.cor = ""
        self.start_date = ""
        self.last_date = ""
        self.file = ""


    def con_click(self, open_second_window):
        cor = self.cor_edit.text()
        start_d = self.start_edit.text()
        last_d = self.fin_edit.text()
        from datetime import datetime
        start_date = datetime.strptime(start_d, "%Y-%m-%d") 
        last_date = datetime.strptime(last_d, "%Y-%m-%d") 
        file = str(self.file_edit.currentText())
        storage = self.storage_edit.text()

        # crawling 본격 시작
        self.hide()

        global options
        from turtle import pd
        from crawling_base import crawling_corporation
        from selenium.webdriver.chrome.options import Options
        import selenium
        from selenium import webdriver
        from time import sleep
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_pdf import PdfPages
        import pandas as pd
        import time
        import math
        import datetime
        URL = 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020203#'
        # 시간 측정
        start_time = time.time() 
        math.factorial(1234567) 
        # 시작
        crawl_corporation = crawling_corporation()
        for corporation in [cor]:
            print(f'----------------------Corporation is {corporation}----------------------')
            # Dataframe
            step1_df = pd.DataFrame()
            step2_df = pd.DataFrame()
            step3_df = pd.DataFrame()
            for step_number in ['step1', 'step2', 'step3']:
                driver = webdriver.Chrome(executable_path=chrom_exe, chrome_options=options)
                driver.get(url=URL)
                start = start_date
                last = last_date
                num = 0
                # 시간 반복
                while start <= last: 
                    dates = start.strftime("%Y%m%d") 
                    timee = [int(dates[0:4]), int(dates[4:6]), int(dates[6:8])]
                    week = date(timee[0], timee[1], timee[2]).weekday()   
                    # weekend 일 경우
                    if week in [5,6] :
                        print("Today is weekend. No Data.")
                    else:
                        if step_number == 'step1':
                            dic = crawl_corporation.step1(corporation, driver, num, week, dates)
                            step1_dic = pd.DataFrame([dic])
                            step1_df = pd.concat([step1_df, step1_dic])
                            num += 1
                        elif step_number == 'step2':
                            dic = crawl_corporation.step2(corporation, driver, num, week, dates)
                            step2_dic = pd.DataFrame([dic])
                            step2_df = pd.concat([step2_df, step2_dic])
                            num += 1                   
                        else:
                            dic = crawl_corporation.step3(corporation, driver, num, week, dates)
                            step3_dic = pd.DataFrame([dic])
                            step3_df = pd.concat([step3_df, step3_dic])
                            num += 1
                    start += timedelta(days=1)
                driver.close()
                print(f'----------------------{step_number} is finished----------------------')
            # final dataframe 정리
            final_df = pd.merge(left = step1_df , right = step2_df, how = "inner", on = "Date")
            final_df = pd.merge(left = final_df , right = step3_df, how = "inner", on = "Date")
            row = final_df['Date'].copy()
            
            # 결과물 저장
            if file == 'EXCEL':
                final_df.to_excel(f'{storage}\crawling_{cor}.xlsx')
            elif file == 'CSV':
                final_df.to_csv(f'{storage}\crawling_{cor}.csv')
            else:
                fig, ax =plt.subplots(figsize=(12,4))
                ax.axis('tight')
                ax.axis('off')
                the_table = ax.table(cellText=final_df.values, colLabels=final_df.columns, loc='center')
                pp = PdfPages(f'{storage}\crawling_{cor}.pdf')
                pp.savefig(fig, bbox_inches='tight')
                pp.close()
            # for row_dict in final_df.to_dict(orient="records"):
            #     time = row_dict['Date']
            #     Count_storage(row_dict, corporation, time)
        # 코드 종료
        import time
        import datetime
        end_time = time.time()
        sec = (end_time - start_time) 
        result = datetime.timedelta(seconds=sec) 
        print(f'Corporation : {cor}')
        print(f'Period : {start_date} -- {last_date}')
        print(f"Running Time : {result}")
        import datetime
        print(f'Now : {datetime.datetime.now()}')

        sleep(10)
        driver.quit()
        print('--------------------------------------------Crawling is completed--------------------------------------------')


        # 완료창 띄우기
        self.second = secondwindow()
        self.second.option1.setText(cor)
        self.second.option2.setText(start_d)
        self.second.option3.setText(last_d)
        self.second.option4.setText(file)
        self.second.option5.setText(storage)
        self.second.exec()
        self.show()


#화면을 띄우는데 사용되는 Class 선언
class secondwindow(QDialog, QWidget, form_class_2) :
    def __init__(self) :
        super().__init__()
        self.initUi()
        self.show()


    def initUi(self):
        self.setupUi(self)
        

    def stop_click(self):
        self.close()



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

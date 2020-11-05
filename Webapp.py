from flask import Flask
from markupsafe import escape
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import json

app = Flask(__name__)

@app.route('/search/<string:Consumer_number>')
def get_events(Consumer_number,charset='utf-8'):
    FPjsonList = []
    SCjsonList = []
    SFjsonList = []
    Events_FP = []
    Timestamps_FP = []

    if Consumer_number[:2] =='FP': #This marks the start of the scrape for Flying Parcel
        url = 'https://www.flyingparcel.net.cn/Indexs/Trace/GetParcelTrack'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'www.flyingparcel.net.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {'code': f'{Consumer_number}'}
        json_data = requests.post(url = url,headers = headers,data = data).json()
        print(Consumer_number)
        for ok in json_data:
            Events_FP.append(ok['CustomStateText'])
            Timestamps_FP.append(ok['CreationTime'])
        Events_FP = list(filter(None, Events_FP))
        for ok in range(0,len(Events_FP)):
            FPjsonList.append({"Event" : Events_FP[ok],"Timestamp" : Timestamps_FP[ok]})
        FPjsonList = json.dumps(FPjsonList,ensure_ascii=False).encode('utf-8')
        return FPjsonList

    elif Consumer_number[:2] =='SF':
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get('https://air-gtc.com/WaybillLot.aspx')
        text_box = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/textarea')
        search_button = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/input')

        text_box.send_keys(Consumer_number)
        search_button.click()
        Events_Result = driver.find_elements_by_class_name('txt')
        Timestamp = driver.find_elements_by_class_name('time')
        Events_Series = []
        Timestamp_Series = []
        for i in Events_Result:
            Events_Series.append(i.text)
        for j in Timestamp:
            Timestamp_Series.append(j.text)
        for i in range(0,len(Events_Series)):
            SFjsonList.append({"Event" : Events_Series[i], "Timestamp" : Timestamp_Series[i]})
        SFjsonList = json.dumps(SFjsonList,ensure_ascii=False).encode('utf-8')
        driver.close()
        return SFjsonList 

    else: #This marks the start of the scrape for Shipexs
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get('http://shipexs.cdnchina360.com/track')
        text_box = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/input[1]')
        search_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/input[2]')
        text_box.send_keys(Consumer_number) # inputting the data
        search_button.click()
        Events_Result = driver.find_elements_by_css_selector('div.r_m_three.ft14')
        Timestamp = driver.find_elements_by_css_selector('div.r_m_one.ft14.fl')
        Events_Series = []
        Timestamp_Series = []
        print(Consumer_number)
        for i in Events_Result:
            Events_Series.append(i.text)
        for j in Timestamp:
            Timestamp_Series.append(j.text)
        for i in range(0,len(Events_Series)):
            SCjsonList.append({"Event" : Events_Series[i], "Timestamp" : Timestamp_Series[i]})
        driver.close()
        SCjsonList = json.dumps(SCjsonList,ensure_ascii=False).encode('utf-8')
        #This marks the end of the scrape for Shipexs
        return SCjsonList
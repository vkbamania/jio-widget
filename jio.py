from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def getjiodata():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(executable_path="D:\My Pro\jio-widget\Resources\chromedriver.exe")
    driver = webdriver.Chrome(executable_path="D:\My Pro\jio-widget\Resources\chromedriver.exe",   chrome_options=chrome_options)
    driver.get("https://www.jio.com/Jio/portal/jioLogin")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pt1:r1:0:sb11:gl1"))
    ).click()
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME, 'pt1:r1:1:sb11:it1'))
    ).send_keys('vineetbamania@gmail.com')
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME, 'pt1:r1:1:sb11:it2'))
    ).send_keys('kapildev1993')
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, 'pt1:r1:1:sb11:cb1'))
    ).click()
    #
    # myNumber = WebDriverWait(driver,10).until(
    #     EC.presence_of_element_located((By.ID, 'pt1:r1:0:pgl117'))
    # )
    # mybal = WebDriverWait(driver,10).until(
    #     EC.presence_of_element_located((By.ID, 'pt1:r1:0:pgl59'))
    # )
    forvoice = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, 'pt1:r1:0:r2:1:lstVoice:0:pgl8'))
    )
    fordata = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, 'pt1:r1:0:r2:1:lstData:0:pgl3'))
    )
    forsms = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, 'pt1:r1:0:r2:1:lstSMS:0:pgl9'))
    )
    # myplan = WebDriverWait(driver,10).until(
    #     EC.presence_of_element_located((By.ID, 'pt1:r1:0:r1:1:i1:0:pgl17'))
    # ).find_element_by_id('pt1:r1:0:r1:1:i1:0:pgl7')
    # exhaust = WebDriverWait(driver,10).until(
    #     EC.presence_of_element_located((By.ID, 'pt1:r1:0:r1:1:i1:0:pgl16'))
    # )
    # mynum = myNumber.find_element_by_class_name('serviceText').text
    # mybalance = mybal.find_element_by_class_name('myAccBalText').text
    balance = forvoice.find_element_by_class_name('leftValueText').text
    balancerenew = forvoice.find_element_by_id('pt1:r1:0:r2:1:lstVoice:0:pgl54').find_element_by_class_name('durationText').text
    remainingdata = fordata.find_element_by_class_name('leftValueText').text
    totaldata = fordata.find_element_by_class_name('totalValueText').text
    datarenew = fordata.find_element_by_id('pt1:r1:0:r2:1:lstData:0:pgl56').find_element_by_class_name('durationText').text
    remainingsms = forsms.find_element_by_class_name('leftValueText').text
    totalsms = forsms.find_element_by_class_name('totalValueText').text
    smsrenew = forsms.find_element_by_id('pt1:r1:0:r2:1:lstSMS:0:pgl58').find_element_by_class_name('durationText').text
    # plan = myplan.find_element_by_class_name('myAppPlanOTUL').text
    # tilldate = exhaust.find_element_by_class_name('hoverExhaustText').text


    context = {}

    # context['PhoneNumber'] = mynum
    # context['Balance'] = mybalance
    context['VoiceBalance'] = balance
    context['VoiceBalanceRenew'] = balancerenew
    context['DataBalanceRemaining'] = remainingdata
    context['DataBalanceTotal'] = totaldata
    context['DataBalanceRenew'] = datarenew
    context['SMSBalanceRemaining'] = remainingsms
    context['SMSBalanceTotal'] = totalsms
    context['SMSBalanceRenew'] = smsrenew
    # context['Plan'] = plan
    # context['Validity'] = tilldate

    # print (context)
    return json.dumps(context)

# getjiodata()

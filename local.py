from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def getlocaljiodata():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="D:\My Pro\jio-widget\Resources\chromedriver.exe",   chrome_options=chrome_options)
    driver.get("http://jiofi.local.html")
    batterylevel = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "batterylevel"))
    ).get_attribute('value')
    batterystatus = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "batterystatus"))
    ).get_attribute('value')
    signalstrength = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "signalstrength"))
    ).get_attribute('value')
    ulrate = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ulCurrentDataRate"))
    ).get_attribute('value')
    dlrate = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dlCurrentDataRate"))
    ).get_attribute('value')
    conntime = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ConnectionTime"))
    ).get_attribute('value')
    imsi = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "imsi"))
    ).get_attribute('value')
    devicemodel = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "devicemodel"))
    ).get_attribute('value')
    connstatus = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "connectedStatus"))
    ).get_attribute('value')
    noOfClient = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "noOfClient"))
    ).get_attribute('value')
    context = {}
    context['BatteryLevel'] = batterylevel
    context['BatteryStatus'] = batterystatus
    context['SignalStrength'] = signalstrength
    context['UploadRate'] = ulrate
    context['DownloadRate'] = dlrate
    context['ConnectionTime'] = conntime
    context['IMSI'] = imsi
    context['DeviceModel'] = devicemodel
    context['ConnectionStatus'] = connstatus
    context['NoOfClients'] = noOfClient

    # print (context)
    return json.dumps(context)

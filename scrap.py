from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from selenium.webdriver.common.by import By
url="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("C:/Users/raina/Downloads/chromedriver_win32/chromedriver")
browser.get(url)
time.sleep(10)
def scrapTheData():
    headers=["Name","Light-years from Earth","Planet Mass","Stellar Magnitude","Discovery Date"]
    planetData=[]
    for i in range(0,5):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        allultags=soup.find_all("ul",attrs={"class","exoplanet"})
        for eachul in allultags:
            alllitags=eachul.find_all("li")
            templist=[]
            for index,eachli in enumerate(alllitags):
                if index==0:
                    templist.append(eachli.find_all("a")[0].contents[0])
                else:
                    templist.append(eachli.contents[0])
            planetData.append(templist)
        browser.find_element(By.XPATH,'//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("strapper.csv","w",newline='') as X:
        csvwriter=csv.writer(X)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetData)
scrapTheData()
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(starturl)
time.sleep(10)
def scrape():
    headers=["Name","Distance","Mass","Radius"]
    planetdata=[]
    for i in range(0,198):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ultag in soup.find_all("ul",attrs={"class","wikipedia"}):
            litags=ultag.find_all("li")
            templist=[]
            for index,litag in enumerate(litags):
                if index==0:
                    templist.append(litag.find_all("a")[0].contents[0])
                    
                else:
                    try:
                        templist.append(litag.contents[0])

                    except:
                        templist.append("")

            planetdata.append(templist)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    with open("scraper.csv","w") as f:
        c=csv.writer(f)
        c.writerow(headers)
        c.writerows(planetdata)

scrape()
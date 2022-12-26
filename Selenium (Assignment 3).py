#!/usr/bin/env python
# coding: utf-8

# # Q1 Write a python program which searches all the product under a particular product from www.amazon.in. The product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for guitars.

# In[1]:


#importing required libraries
import selenium
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import re


# In[2]:


#connecting to the webdriver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[3]:


#maximizing the window
driver.maximize_window()


# In[4]:


#opening the amazon website on automated edge browser
driver.get("https://www.amazon.in/")

time.sleep(3)


# In[5]:


#Asking the user for the search input
search=input("Enter keyword, you wanted to search on Amazon.in website:")


# In[6]:


#entering the search word as per requirement
searching=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
searching.send_keys(search)


# In[7]:


#clicking on search button
clicking=driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
clicking.click()


# In[ ]:





# #  Q2  In the above question, now scrape the following details of each product listed in first 3 pages of your search results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then scrape all the products available under that product name. Details to be scraped are: "Brand Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“.

# In[8]:


# fetching URLs to open the pages
urls = []          # empty list
for i in range(0,3):      # for loop to scrape 3 pages
    page_url = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in page_url:
        urls.append(i.get_attribute("href"))
    next_btn = driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    time.sleep(3)


# In[10]:


len(urls)


# In[12]:


#Creating the empty lists for saving the details to list
Brand_Name=[]
Name_of_Product=[]
Price=[]
Return_Exchange=[]
Expected_Delivery=[]
Availability=[]

#using for loop to get the details of all the guitars from their URLs
for i in urls:
    driver.get(i)
    time.sleep(1)
    
    #to fetch the Brand Names
    try:
        brand=driver.find_element(By.XPATH,'//tr[@class="a-spacing-small po-brand"]')
        Brand_Name.append(brand.text)
    except NoSuchElementException:
        Brand_Name.append('-')
        
    #to fetch the product names   
    try:
        product=driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]')
        Name_of_Product.append(product.text)
    except NoSuchElementException:
        Name_of_Product.append('-')
        
    
    #to fetch the prices
    try:
        Prices=driver.find_element(By.XPATH,'//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]')
        Price.append(Prices.text)
    except NoSuchElementException:
        Price.append('-')
        
    
    #to fetch the return or exhange policy
    try:
        Return=driver.find_element(By.XPATH,'//*[@id="RETURNS_POLICY"]/span/div[2]/a')
        Return_Exchange.append(Return.text)
    except NoSuchElementException:
        Return_Exchange.append('-')
        
    
    #to fetch the delivery time
    try:
        delivery=driver.find_element(By.XPATH,'//*[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]/span/span[1]')
        Expected_Delivery.append(delivery.text)
    except NoSuchElementException:
        Expected_Delivery.append('-')
        
    
    #to fetch the stock availability
    try:
        stock=driver.find_element(By.XPATH,'//*[@id="availability"]/span')
        Availability.append(stock.text)
    except NoSuchElementException:
        Availability.append('-')
        
        


# In[13]:


#to check the content length of each of the lists
len(Brand_Name),len(Name_of_Product),len(Price),len(Return_Exchange),len(Expected_Delivery),len(Availability)


# In[14]:


Guitar=pd.DataFrame({"Brand_Name":Brand_Name,"Name_of_Product":Name_of_Product,"Price":Price,"Return/Exchange":Return_Exchange,"Expected Delivery":Expected_Delivery,"Availability":Availability})
Guitar


# In[16]:


Guitar.to_csv('Guitar.csv')
driver.close()


# In[ ]:





# # Q3.Write a python program to access the search bar and search button on images.google.com and scrape 10 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’.

# In[1]:


#importing required libraries
import selenium
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import re


# In[168]:


#connecting to the webdriver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[169]:


#maximizing the window
driver.maximize_window()


# In[170]:


#opening the images.google.com website on automated edge browser
driver.get("https://images.google.com/")

time.sleep(3)


# In[171]:


List_KeyWords=("fruits","cars","Machine Learning","Guitar","Cakes")


# In[172]:


List_KeyWords


# In[174]:


# geting the webpage of mentioned url
url = "http://images.google.com/"

# creating empty list
urls = []
data = []

search_item = ["Fruits","Cars","Machine Learning","Guitar","Cakes"]
for item in search_item:
    driver.get(url)
    time.sleep(3)
    
    # finding webelement for search_bar
    search_bar = driver.find_element(By.TAG_NAME,"input")
    
    # sending keys to get the keyword for search bar
    search_bar.send_keys(str(item))
    
    # clicking on search button
    search_button = driver.find_element(By.XPATH,"//button[@class='Tg7LZd']")
    search_button.click()
    
    # scroling down the webpage to get some more images
    for _ in range(500):
        driver.execute_script("window.scrollBy(0,100)")
        
        imgs = driver.find_elements(By.XPATH,"//img[@class='rg_i Q4LuWd']")
    img_url = []
    for image in imgs:
        source = image.get_attribute('src')
        if source is not None:
            if(source[0:4] == 'http'):
                img_url.append(source)
    for i in img_url[:10]:
        urls.append(i)
        
for i in range(len(urls)):
    if i >= 10:
        break
    print("Downloading {0} of {1} images" .format(i,10))
    response = requests.get(urls[i])
    
    file = open(r'C:\Users\invra\Untitled Folder'+str(i)+".jpg","wb")

    file.write(response.content)


# In[ ]:





# # Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on
# www.flipkart.com and scrape following details for all the search results displayed on 1st page. Details to be 
# scraped: “Brand Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, 
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the 
# details is missing then replace it by “- “. Save your results in a dataframe and CSV.

# In[1]:


#importing required libraries
import selenium
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By


# In[11]:


#connecting to the webdriver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")

#maximizing the window
driver.maximize_window()


# In[12]:


# getting the webpage of mentioned url
driver.get("https://www.flipkart.com/")


# In[13]:


# closing login popup button
login = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button")
login.click()


# In[14]:


#to search for One Plus Nord

search=driver.find_element(By.XPATH,'//input[@class="_3704LK"]')
search.send_keys("OnePlus Nord")

#clicking on the search icon
search_button=driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
search_button.click()


# In[15]:


#to get the product UrLs of all the products listed in page 1
Product_URL=[]
URL=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in URL:
    Product_URL.append(i.get_attribute('href'))


# In[16]:


len(Product_URL)


# In[21]:


#Creating empty lists for saving all the required details in to lists
Brand_Name=[]
Smartphone_Name=[]
Colour=[]
RAM=[]
Storage_ROM=[]
Primary_Camera=[]
Secondary_Camera=[]
Display_Size=[]
Battery_Capacity=[]
Price=[]


#fetaching the required details from each listed item from their URLS exctracted above

for i in Product_URL:
    driver.get(i) 
    #to click on the read more option to get all details to scrap
    read_more=driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    read_more.click()
    
    #to fetch the Brand Name
    try:
        Brand=driver.find_element(By.XPATH,'//span[@class="B_NuCI"]')
        Brand_Name.append(Brand.text.split()[0])
    except NoSuchElementException:
        Brand_Name.append('-')
        
        
    #to fetch smartPhone Name
    try:
        name_tags = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][1]/table/tbody/tr[3]/td[2]/ul/li")
        Smartphone_Name.append(name_tags.text)
    except NoSuchElementException:
        Smartphone_Name.append('-')
        
    
    #to fetch phone colour option
    try:
        color=driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][1]/table/tbody/tr[4]/td[2]/ul/li")
        Colour.append(color.text)
    except NoSuchElementException:
        Colour.append('-')
        
        
    #to fetch RAM
    try:
        RAMs=driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][4]/table[1]/tbody/tr[2]/td[2]/ul/li")
        RAM.append(RAMs.text)
    except NoSuchElementException:
        RAM.append('-')
        
        
    #to fetch storage ROM
    try:
        ROM=driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][4]/table[1]/tbody/tr[1]/td[2]/ul/li")
        Storage_ROM.append(ROM.text)
    except NoSuchElementException:
        Storage_ROM.append('-')
        
        
        
    #to fetch Primary_Camera of the phone
    try:
        Pri_cam=driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[2]/td[2]/ul/li")
        Primary_Camera.append(Pri_cam.text)
    except NoSuchElementException:
        Primary_Camera.append('-')
        
        
          
    # to fetch secondary camera of the phone
    try:
        sec = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[6]/td[1]")
        if sec != 'Secondary Camera' :
            if driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[5]/td[1]").text == "Secondary Camera":
                sec_cam =driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[5]/td[2]/ul/li")
            else :
                raise NoSuchElementException
        else :
            sec_cam = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[6]/td[2]/ul/li")
        Secondary_Camera.append(sec_cam.text)
    except NoSuchElementException:
        Secondary_Camera.append('-')
        
        
        
    #to fetch Display_Size
    try:
        disp = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][2]/div")
        if disp.text != 'Display Features' : raise NoSuchElementException
        disp_size = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][2]/table[1]/tbody/tr[1]/td[2]/ul/li")
        Display_Size.append(disp_size.text)
    except NoSuchElementException:
        Display_Size.append('-')
        
        
        
    #to fetch battery capacity
    try:
        if driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][10]/div").text != "Battery & Power Features" :
            if driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][9]/div").text == "Battery & Power Features" :
                bat_tags = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][9]/table/tbody/tr/td[1]")
                if bat_tags.text != "Battery Capacity" : raise NoSuchElementException
                bat_capa = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][9]/table/tbody/tr/td[2]/ul/li")
            elif driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][8]/div").text == "Battery & Power Features" :
                bat_tags = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][8]/table/tbody/tr/td[1]")
                if bat_tags.text != "Battery Capacity" : raise NoSuchElementException
                bat_capa = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][8]/table/tbody/tr/td[2]/ul/li")
            else:
                raise NoSuchElementException
        else :
            bat_tags = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][10]/table/tbody/tr/td[1]")
            if bat_tags.text != "Battery Capacity" : raise NoSuchElementException
            bat_capa = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][10]/table/tbody/tr/td[2]/ul/li")
        Battery_Capacity.append(bat_capa.text)
    except NoSuchElementException:
        Battery_Capacity.append('-')
        
        
        
    #to fetch price
    try:
        price_tags = driver.find_element(By.XPATH,"//div[@class='_30jeq3 _16Jk6d']")
        Price.append(price_tags.text)
    except NoSuchElementException:
        Price.append('-')


# In[22]:


len(Brand_Name),len(Smartphone_Name),len(Colour),len(RAM),len(Storage_ROM),len(Primary_Camera),len(Secondary_Camera),len(Display_Size),len(Battery_Capacity),len(Price)


# In[23]:


#creating the pandas data frame
SmartPhones=pd.DataFrame({"Brand_Name":Brand_Name,"Smartphone_Name":Smartphone_Name,"Colour":Colour,"RAM":RAM,"Storage_ROM":Storage_ROM,"Primary_Camera":Primary_Camera,"Secondary_Camera":Secondary_Camera,"Display_Size":Display_Size,"Battery_Capacity":Battery_Capacity,"Price":Price})
SmartPhones


# In[24]:


# saving the data into a csv file
SmartPhones.to_csv("SmartPhones.csv")


# In[25]:


driver.close()


# # Q5 Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

# In[2]:


#importing required libraries
import selenium
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import re


# In[53]:


#connecting to the webdriver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[54]:


#maximizing the window
driver.maximize_window()


# In[55]:


#opening the maps.google.co.in website on automated edge browser
driver.get("https://www.google.co.in/maps")

time.sleep(3)


# In[56]:


search_word=input("enter the search city name:")
search=driver.find_element(By.XPATH,'//input[@class="searchboxinput xiQnY"]')
search.send_keys(search_word)
button=driver.find_element(By.XPATH,'//button[@class="mL3xi"]')
button.click()


# In[73]:



try:
    url_string = driver.current_url
    print("URL Extracted: ", url_string)
    lat_long = re.findall(r'@(.*)data',url_string)
    if len(lat_long):
        lat_long_list = lat_long[0].split(",")
        if len(lat_long_list)>=2:
            latitude = lat_long_list[0]
            longitude = lat_long_list[1]
        print("Latitude = {}, Longitude = {}".format(latitude, longitude))
except Exception as e:
        print("Error: ", str(e))


# In[ ]:





# # Q6 Write a program to scrap details of all the funding deals for second quarter (i.e Jan 21 – March 21) from trak.in.

# In[92]:


#importing required libraries
import selenium
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import re


# In[93]:


#connecting to the webdriver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[94]:


#maximizing the window
driver.maximize_window()


# In[95]:


#opening the trak.in website on automated edge browser
driver.get("https://www.trak.in/")

time.sleep(3)


# In[96]:


#to click on the funding deals option
funding=driver.find_element(By.XPATH,'//li[@class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1237902"]')
funding.click()


# In[14]:


#not getting data in funding deals option


# In[ ]:





# # Q7.Write a program to scrap all the available details of best gaming laptops from digit.in.

# In[48]:


#importing required libraries
import selenium
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import re
from selenium.webdriver.support.ui import WebDriverWait


# In[16]:


#connecting to the webdriver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[17]:


#maximizing the window
driver.maximize_window()


# In[18]:


#opening the digit.in website on automated edge browser
driver.get("https://www.digit.in/")

time.sleep(3)


# In[25]:


#for clicking on the best gaming laptops link
Gaming_Laptops=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div[2]/div[4]/ul/li[9]")
Gaming_Laptops.click()


# In[44]:


#creating empty lists and saving the deails to each list

#Laptop_Name=[]

#Name=driver.find_elements(By.TAG_NAME,'h3')
#for i in Name:
    #Laptop_Name.append(i.text)
    
#Laptop_Name


# In[53]:


# fetching URLs to open the pages
urls=[]          # empty list
    # for loop to scrape all the urls
laptop_url=driver.find_elements(By.XPATH,'//span[@class="datahreflink spec"]')
for i in laptop_url:
    urls.append(i.get_attribute("data-href"))


# In[54]:


urls


# In[80]:


#creating empty lists for saving the details
Name=[]
Operating_System=[]
Display=[]
Processor=[]
Memory=[]
Release_Date=[]
Starting_Price=[]
Weight=[]
Rating=[]
Dimensions=[]

#using for loop to get the details of the each laptop
for i in urls:
    driver.get(i)
    time.sleep(3)
    
    #Scraping brand name 
    try:
        brand = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/h1")
        Name.append(brand.text)
    except NoSuchElementException:
        Name.append('-')
    
    
    #Scraping the OS
    try:
        OS=driver.find_element(By.XPATH,'//*[@id="overview"]/div[2]/div[3]/div/ul/li[1]/div/p[2]/strong')
        Operating_System.append(OS.text)
    
    except NoSuchElementException:
        Operating_System.append('-')
        
        
    #Scraping Display
    try:
        Displays=driver.find_element(By.XPATH,'//*[@id="overview"]/div[2]/div[3]/div/ul/li[2]/div/p[2]/strong')
        Display.append(Displays.text)
        
    except NoSuchElementException:
        Display.append('-')
        
    #scraping the processor
    try:
        Proc=driver.find_element(By.XPATH,'//*[@id="overview"]/div[2]/div[3]/div/ul/li[3]/div/p[2]/strong')
        Processor.append(Proc.text)
        
    except NoSuchElementException:
        Processor.append('-')
        
    #Scraping Memory
    try:
        Mem=driver.find_element(By.XPATH,'//*[@id="overview"]/div[2]/div[3]/div/ul/li[4]/div/p[2]/strong')
        Memory.append(Mem.text)
        
    except NoSuchElementException:
        Memory.append('-')
        
     
    #scraping release year & Month
    try:
        Release=driver.find_element(By.XPATH,'//*[@id="overview"]/div[2]/div[1]/div[2]/strong')
        Release_Date.append(Release.text)
        
    except NoSuchElementException:
        Release_Date.append('NA')
        
    #scraping the price details   
    try:
        Prices=driver.find_element(By.XPATH,'//*[@id="overview"]/div[2]/div[4]/div/h2/strong')
        Starting_Price.append(Prices.text)
    
    except NoSuchElementException:
        Starting_Price.append('NA')
        
        
    #scraping weight
    try:
        weigh=driver.find_element(By.XPATH,'//*[@id="specs"]/div/div[1]/div[5]/table/tbody/tr[1]/td[3]')
        Weight.append(weigh.text)
        
    except NoSuchElementException:
        Weight.append('NA')
    

    #scraping rating
    try:
        Ratings=driver.find_element(By.XPATH,'//*[@id="user_review"]/div[3]/div[1]/div[1]/div')
        Rating.append(Ratings.text)
        
    except NoSuchElementException:
        Rating.append('NA')
        
        
    #Scraping Dimensions
    try:
        Dimen=driver.find_element(By.XPATH,'//*[@id="specs"]/div/div[1]/div[5]/table/tbody/tr[2]/td[3]')
        Dimensions.append(Dimen.text)
        
    except NoSuchElementException:
        Dimensions.append('NA')


# In[82]:


#creating pandas data frame and saving the details to it

Top_Gaming_Laptops=pd.DataFrame({'Name':Name,'Release_Date':Release_Date,'Operating_System':Operating_System,'Display':Display,'Processor':Processor,'Memory':Memory,'Starting_Price':Starting_Price,'Weight':Weight,'Dimensions':Dimensions,'Rating':Rating})
Top_Gaming_Laptops


# In[83]:


Top_Gaming_Laptops.to_csv('Top_Gaming_Laptops.csv')
driver.close()


# In[ ]:





# # Q8.Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”.

# In[1]:


#importing required libraries
import selenium
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import re
from selenium.webdriver.support.ui import WebDriverWait


# In[2]:


#connecting to the webdriver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[3]:


#maximizing the window
driver.maximize_window()


# In[4]:


#opening the forbes.com website on automated edge browser
driver.get("https://www.forbes.com/")

time.sleep(3)


# In[5]:


#To click on the left side hamburger menu
menu=driver.find_element(By.XPATH,'//*[@id="globalHeaderMenu"]/div')
menu.click()
time.sleep(1)


# In[6]:


#To click on the nillionaires option
option=driver.find_element(By.XPATH,'//*[@id="globalHeaderMenu"]/div/div[2]/ul/li[1]/div[1]')
option.click()
time.sleep(1)


# In[7]:


#to click view all billionaires (worlds billionaires) option
allb=driver.find_element(By.XPATH,'//*[@id="row-1"]/div/div/div[1]/div/div[1]/div[1]/div[2]/a/h2')
allb.click()


# In[8]:


#Creating empty lists
Rank=[]
Name=[]
NetWorth=[]
Age=[]
Citizenship=[]
Source=[]
Industry=[]

#Using for loop to scrap the all 14 pages

for i in range(14):
    
    #to get the Ranks of the billionaires scraped
    Ranks=driver.find_elements(By.XPATH,'//div[@class="rank"]')
    for i in Ranks:
        Rank.append(i.text)
        
    #to get the names of the billionaires scraped
    Names=driver.find_elements(By.XPATH,'//div[@class="personName"]')
    for i in Names:
        Name.append(i.text)
        
    #to get the Networth
    NetWorths=driver.find_elements(By.XPATH,'//div[@class="netWorth"]')
    for i in NetWorths:
        NetWorth.append(i.text)
        
    #to get the Age 
    Ages=driver.find_elements(By.XPATH,'//div[@class="age"]')
    for i in Ages:
        Age.append(i.text)
        
    #to get the citizenship details
    Citi=driver.find_elements(By.XPATH,'//div[@class="countryOfCitizenship"]')
    for i in Citi:
        Citizenship.append(i.text)
        
    #to get the source details
    sources=driver.find_elements(By.XPATH,'//div[@class="source-column"]')
    for i in sources:
        Source.append(i.text)
        
    #to get the Industry details
    Industries=driver.find_elements(By.XPATH,'//div[@class="category"]')
    for i in Industries:
        Industry.append(i.text)
    
#time.sleep(3)

#going to next page
Next_Page=driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[27]/div[2]/div[6]/div[1]/button[2]/div/span')
Next_Page.click()


# In[9]:


len(Rank),len(Name),len(NetWorth),len(Age),len(Citizenship),len(Source),len(Industry)


# In[10]:


#creating pandas data frame and saving the data
Billionaires=pd.DataFrame({"Rank":Rank,"Name":Name,"NetWorth":NetWorth,"Age":Age,"Citizenship":Citizenship,"Source":Source,"Industry":Industry})
Billionaires


# In[11]:


Billionaires.to_csv('Billionaires.csv')
driver.close()


# # Q9.Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted from any YouTube Video.

# In[101]:


#importing required libraries
import selenium
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import re
from selenium.webdriver.support.ui import WebDriverWait


# In[102]:


#connecting to the webdriver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[103]:


#maximizing the window
driver.maximize_window()


# In[104]:


#opening the youtube.com website on automated edge browser
driver.get("https://www.youtube.com/")

time.sleep(3)


# In[105]:


#entering search term for a video
search=driver.find_element(By.XPATH,'//div[@class="ytd-searchbox-spt"]/input')
search.send_keys('GOT')

#clicking on search button
button=driver.find_element(By.ID,'search-icon-legacy')
button.click()


# In[106]:


#clicking on the first video
video=driver.find_element(By.XPATH,'//yt-formatted-string[@class="style-scope ytd-video-renderer"]')
video.click()


# In[117]:


# 10000 times we scroll down by 10000 in order to generate more comments
for _ in range(1000):
    driver.execute_script("window.scrollBy(0,10000)")


# In[118]:


#make empty lists
comments = []
comment_time = []
Time = []
Likes = []
No_of_Likes = []


# In[133]:


#scraping the data of comments
cm_tags = driver.find_elements(By.XPATH,'//*[@id="content-text"]')
for cm in cm_tags:
    if cm.text is None:
        comments.append("--")
    else:
        comments.append(cm.text)
time.sleep(5)


# In[134]:


# scraping the data of time when comment was posted
tm_tags = driver.find_elements(By.XPATH,"//a[contains(text(),'ago')]")
for tm in tm_tags:
    Time.append(tm.text)

for i in range(0,len(Time),2):
    comment_time.append(Time[i])
time.sleep(8)


# In[135]:


# scraping the data of comment likes
like_tags = driver.find_elements(By.XPATH,"//span[@class='style-scope ytd-comment-action-buttons-renderer']")
for like in like_tags:
    Likes.append(like.text)
    
for i in range(1,len(Likes),2):
    No_of_Likes.append(Likes[i])
    
time.sleep(8)


# In[136]:


len(No_of_Likes),len(comments),len(comment_time)


# In[138]:


#Creating dataframe
Youtube=pd.DataFrame({})
Youtube['Comments'] = comments[0:500]
Youtube['Comment_time'] = comment_time[0:500]
Youtube['Comment upvotes'] = No_of_Likes[0:500]


# In[139]:


Youtube


# In[ ]:





# # Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall reviews, privates from price, dorms from price, facilities and property description.

# In[146]:


#importing required libraries
import selenium
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import re
from selenium.webdriver.support.ui import WebDriverWait


# In[147]:


#connecting to the webdriver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[148]:


#maximizing the window
driver.maximize_window()


# In[149]:


#opening the hostelworld.com website on automated edge browser
driver.get("https://www.hostelworld.com/")

time.sleep(3)


# In[151]:


# locating the location search bar
search_bar = driver.find_element(By.XPATH,'//*[@id="search-input-field"]')

# entering London in search bar
search_bar.send_keys("London")


# In[152]:


# select London
London = driver.find_element(By.XPATH,'//*[@id="predicted-search-results"]/li[2]')
#clicking on button
London.click()

# do click on Let's Go button
search_btn = driver.find_element(By.ID,'search-button')
search_btn.click()


# In[153]:


#lets find required data
hostel_name = []
distance = []
pvt_prices = []
dorms_price = []
rating = []
reviews = []
over_all = []
facilities = []
description =[]
product_url = []


# In[167]:


#Scraping the requered informations
for i in range(2):

    #fetching hostel name
    try:
        name = driver.find_elements(By.XPATH,"//h2[@class='title title-6']")
        for i in name:
            hostel_name.append(i.text)
    except NoSuchElementException:
        hostel_name.append('-')
    #fetching distance from city centre
    
    try:
        dist = driver.find_elements(By.XPATH,"//div[@class='subtitle body-3']//a//span[1]")
        for i in dist:
            distance.append(i.text.replace('Hostel - ',''))
    except NoSuchElementException:
        distance.append('-')
        
    for i in driver.find_elements(By.XPATH,"//div[@class='prices-col']"):
    #fetch privates from price
        try:
            pvt_price = driver.find_element(By.XPATH,"//a[@class='prices']//div[1]//div")
            pvt_prices.append(pvt_price.text)
        except NoSuchElementException:
            pvt_prices.append('-')
    #fetching dorms from price
    for i in driver.find_elements(By.XPATH,"//div[@class='prices-col']"):
        try:
            dorms = driver.find_element(By.XPATH,"//a[@class='prices']//div[2]//div")
            dorms_price.append(dorms.text)
        except NoSuchElementException:
            dorms_price.append('-')
            #fetching facilities
    try:
        fac1 = driver.find_elements(By.XPATH,"//div[@class='has-wifi']")
        fac2 = driver.find_elements(By.XPATH,"//div[@class='has-sanitation']")
        for i in fac1:
            for j in fac2:
                facilities.append(i.text +', '+ j.text )
    except NoSuchElementException:
        facilities.append('-')
    #lets fetch url of each hostel
    p_url = driver.find_elements(By.XPATH,"//div[@class='prices-col']//a[2]")
    for i in p_url:
        product_url.append(i.get_attribute('href'))

for i in product_url:
    driver.get(i)
    time.sleep(3)
    #lets click on show more button for description
    #try:
        #driver.find_element(By.XPATH,"//a[@class='toggle-content']").click()
        #time.sleep(5)
    #except NoSuchElementException:
        #pass
    #fetching ratings
    try:
        rat = driver.find_element(By.XPATH,"//div[@class='score orange big' or @class='score gray big']")
        rating.append(rat.text)
    except NoSuchElementException:
        rating.append('-')
    #fetching total reviews
        
    try:
        rws = driver.find_element(By.XPATH,"//div[@class='reviews']")
        reviews.append(rws.text.replace('Total Reviews',''))
    except NoSuchElementException:
        reviews.append('-')
        #fetch overall review
    try:
        overall_rw = driver.find_element(By.XPATH,"//div[@class='keyword']//span")
        over_all.append(overall_rw.text)
    except NoSuchElementException:
        over_all.append('-')
    #fetch property description 
    try:
        disc = driver.find_element(By.XPATH,"//div[@class='content']")
        description.append(disc.text)
    except NoSuchElementException:
        over_all.append('-')
        
try:        
    button=driver.find_element(By.XPATH,"//div[@class = 'pagination-item pagination-current' or @class='pagination-item']")
    button.click()
except NoSuchElementException:
    
    print("Done")
time.sleep(4)


# In[165]:


#Creating dataframe
Hotels = pd.DataFrame({})
Hotels['Hostel_Name'] = hostel_name
Hotels['Distance fron city centre'] = distance
Hotels['Ratings'] = rating
Hotels['Total_reviews'] = reviews
Hotels['Overall Reviews'] = over_all
Hotels['Privates from price'] = pvt_prices
Hotels['Dorms from price'] = dorms_price
Hotels['Facilities'] = facilities[:60]
Hotels['Description'] = description


# In[166]:


Hotels


# In[ ]:





# In[ ]:





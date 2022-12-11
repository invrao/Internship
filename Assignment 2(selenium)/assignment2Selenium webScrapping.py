#!/usr/bin/env python
# coding: utf-8

# In[1]:


#installling selenium
get_ipython().system('pip install selenium')


# In[1]:


#importing the required libraries
import selenium
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[2]:


#connecting to the driver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[3]:


#opening the naukri website on automated edge browser
driver.get("https://www.naukri.com/")


# In[4]:


#entering the designation and location as per the search requirement
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Analyst')


# In[5]:


#sending bangalore location for search
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[6]:


#clicking the search button
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[19]:


#creating empty lists for storing the data scraping
Job_Title=[]
Job_Location=[]
Company_Name=[]
Experience_Required=[]


# In[20]:


#Scraping Job Title from the page
Title_Tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in Title_Tags[0:10]:
    Title=i.text
    Job_Title.append(Title)
    

#scraping the job location
Location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 locWdth"]')
for i in Location_tags[0:10]:
    Location=i.text
    Job_Location.append(Location)
    
#Scraping the Company name
Comp_name=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Comp_name[0:10]:
    comp=i.text
    Company_Name.append(comp)
    
#scraping Experience Required
Exp=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 expwdth"]')
for i in Exp[0:10]:
    Ex=i.text
    Experience_Required.append(Ex)
    


# In[22]:


#creating a pandas data drame and calling it
DA_Jobs=pd.DataFrame({"Job_Title":Job_Title,"Job_Location":Job_Location,"Company_Name":Company_Name,"Experience_Required":Experience_Required})
DA_Jobs


# In[ ]:





# # Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.

# In[23]:


#importing the required libraries
import selenium
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[24]:


#connecting to the driver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[25]:


#opening the naukri website on automated edge browser
driver.get("https://www.naukri.com/")


# In[29]:


#entering the designation and location as per the search requirement and going for automated browsing
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')

#sending location for search
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')

#clicking search button
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[30]:


#Creating Empty list for storing the search results
Job_Title=[]
Job_Location=[]
Company_Name=[]
Experience_Required=[]


# In[31]:


#Scraping Job Title from the page
Title_Tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in Title_Tags[0:10]:
    Title=i.text
    Job_Title.append(Title)
    

#scraping the job location
Location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 locWdth"]')
for i in Location_tags[0:10]:
    Location=i.text
    Job_Location.append(Location)
    
#Scraping the Company name
Comp_name=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Comp_name[0:10]:
    comp=i.text
    Company_Name.append(comp)
    
#scraping Experience Required
Exp=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 expwdth"]')
for i in Exp[0:10]:
    Ex=i.text
    Experience_Required.append(Ex)
    


# In[32]:


#Creating the Pandas Data Frame and saving the results in data FRame
DS_Jobs=pd.DataFrame({"Job_Title":Job_Title,"Job_Location":Job_Location,"Company_Name":Company_Name,"Experience_Required":Experience_Required})
DS_Jobs


# In[ ]:





# # Q3: In this question you have to scrape data using the filters available on the webpage as shown below:
# #You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results. You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs

# In[33]:


#importing the required libraries
import selenium
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[34]:


#connecting to the driver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[35]:


#opening the naukri website on automated edge browser
driver.get("https://www.naukri.com/")


# In[36]:


#entering the designation as per the search requirement and going for automated browsing
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')

#clicking search button
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[37]:


#For clicking the Delhi NCR location in filters

location=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/i')
location.click()


# In[38]:


#for selecting the 3-6lakhs salary filter

Salary=driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/p/span[1]')
Salary.click()


# In[39]:


#Creating Empty list for storing the search results
Job_Title=[]
Job_Location=[]
Company_Name=[]
Experience_Required=[]


# In[40]:


#Scraping Job Title from the page
Title_Tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in Title_Tags[0:10]:
    Title=i.text
    Job_Title.append(Title)
    

#scraping the job location
Location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 locWdth"]')
for i in Location_tags[0:10]:
    Location=i.text
    Job_Location.append(Location)
    
#Scraping the Company name
Comp_name=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Comp_name[0:10]:
    comp=i.text
    Company_Name.append(comp)
    
#scraping Experience Required
Exp=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 expwdth"]')
for i in Exp[0:10]:
    Ex=i.text
    Experience_Required.append(Ex)
    


# In[41]:


#Creating the Pandas Data Frame and saving the results in data FRame
DS_Jobs=pd.DataFrame({"Job_Title":Job_Title,"Job_Location":Job_Location,"Company_Name":Company_Name,"Experience_Required":Experience_Required})
DS_Jobs


# In[ ]:





# # Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. Product Description
# 3. Price
# The attributes which you have to scrape is ticked marked in the below image.

# In[50]:


#importing the required libraries
import selenium
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[51]:


#connecting to the driver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[52]:


#opening the flipkart website on automated edge browser
driver.get("https://www.flipkart.com/")


# In[53]:


#for closing the signin pop up window
popup=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/button')
popup.click()


# In[54]:


#entering Sunglasses in search bar
Sunglass=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
Sunglass.send_keys("sunglasses")

#clicking Search icon
Search=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
Search.click()


# In[71]:


#Creating the empty lists and storing the data extracted
Brand=[]
Product_Description=[]
Price=[]
Discount=[]

#for searching in the 3 pages
for i in range(3):
    Name=driver.find_elements(By.CLASS_NAME,"_2WkVRV")###Extracting the name of the brand
    for i in Name:
        Brand.append(i.text)
        
        
    Prod=driver.find_elements(By.CLASS_NAME,"IRpwTa")###Extracting the Product description
    for i in Prod:
        Product_Description.append(i.text)
        
        
    Rate=driver.find_elements(By.XPATH,"//div[@class='_30jeq3']")###Extracting price
    for i in Rate:
        Price.append(i.text)
        
    Disc=driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')###Extracting the discount
    for i in Disc:
        Discount.append(i.text)
        
        
#for letting the python sleep, till the page loads
time.sleep(3)

#going to next page
Next_Page=driver.find_element(By.CLASS_NAME,'_1LKTO3')
Next_Page.click()


# In[72]:


#checking the length of the data extracted for ensuring same length before making pandas df
len(Brand),len(Product_Description),len(Price),len(Discount)


# In[73]:


#Creating the Pandas Data Frame and saving the results in data FRame
Sunglasses=pd.DataFrame({"Brand":Brand,"Product_Description":Product_Description,"Price":Price,"Discount":Discount})
Sunglasses[0:100]


# In[ ]:





# # Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: https://www.flipkart.com/apple-iphone-11-black-64-gb/product- reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market place=FLIPKART

# In[74]:


#importing the required libraries
import selenium
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[75]:


#connecting to the driver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[77]:


#opening the flipkart website on automated edge browser
iphone11page=driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART")


# In[79]:


#Creating the empty lists and storing the data extracted

Rating=[]
Review_Summary=[]
Full_Review=[]

#for searching in 10 pages
for i in range(10):
    Review_Sum=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')###to get the review summary
    for i in Review_Sum:
        Review_Summary.append(i.text)
        
    Ratings=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')###to get the rating
    for i in Ratings:
        Rating.append(i.text)
        
    Review=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')###to get the full review
    for i in Review:
        Full_Review.append(i.text)
        

#letting the python sleep during page loading        
time.sleep(3)

#for going to next page
Next_Page=driver.find_element(By.CLASS_NAME,'_1LKTO3')
Next_Page.click()


# In[81]:


#checking the length of the data extracted for ensuring same length before making pandas df
len(Rating),len(Review_Summary),len(Full_Review)


# In[82]:


#Creating the Pandas Data Frame and saving the results in data FRame
Reviews=pd.DataFrame({"Rating":Rating,"Review_Summary":Review_Summary,"Full_Review":Full_Review})
Reviews


# In[ ]:





# # Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.
# You have to scrape 4 attributes of each sneaker:
# 1. Brand
# 2. Product Description
# 3. Price

# In[83]:


#importing the required libraries
import selenium
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[84]:


#connecting to the driver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[85]:


#opening the flipkart website on automated edge browser
driver.get("https://www.flipkart.com/")


# In[86]:


#for closing the popup window
popup=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/button')
popup.click()


# In[87]:


#entering sneakers in search bar
Sneakers=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
Sneakers.send_keys("sneakers")

#clicking Search icon
Search=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
Search.click()

time.sleep(3)


# In[97]:


#creating empty list for storing the data
Brand=[]
Product_Description=[]
Price=[]


###for searching in 3 pages
for i in range(3):

    Brands=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')###to get Brand Name
    for i in Brands:
        Brand.append(i.text)
        
        
    Prod_Des=driver.find_elements(By.CLASS_NAME,'IRpwTa')###to get Product description
    for i in Prod_Des:
        Product_Description.append(i.text)
        
        
    Prices=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')###to get Price
    for i in Prices:
        Price.append(i.text)
        
        
# going to next page        
time.sleep(3)
Next_Page=driver.find_element(By.CLASS_NAME,'_1LKTO3')
Next_Page.click()
        


# In[98]:


#checking the length of the data extracted for ensuring same length before making pandas df
len(Brand),len(Product_Description),len(Price)


# In[99]:


#Creating the Pandas Data Frame and saving the results in data FRame
Sneakers=pd.DataFrame({"Brand":Brand,"Product_Description":Product_Description,"Price":Price})
Sneakers[0:100]


# In[ ]:





# # Q7: Go to webpage https://www.amazon.in/
# Enter “Laptop” in the search field and then click the search icon.
# Then set CPU Type filter to “Intel Core i7” as shown in the below image:

# In[104]:


#importing the required libraries
import selenium
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[111]:


#connecting to the driver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[112]:


#opening the amazon website on automated edge browser
driver.get("https://www.amazon.in/")


# In[113]:


#entering Laptop in search bar

search=driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute"]')
search.send_keys("Laptop")

#for clicking the search button

press=driver.find_element(By.XPATH,'//span[@class="nav-search-submit-text nav-sprite nav-progressive-attribute"]')
press.click()


# In[114]:


#to select the core i7 filter

i7=driver.find_element(By.XPATH,'//*[@id="p_n_feature_thirteen_browse-bin/12598163031"]/span/a/span')
i7.click()


# In[124]:


#creating empty list for storing the data

Title=[]
Ratings=[]
Price=[]

##Getting the Titles/laptop names
Title_Tags=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in Title_Tags[0:10]:
    Title.append(i.text)
    

##Getting the Ratings
Rating=driver.find_elements(By.XPATH,'//div[@class="a-row a-size-small"]')
for i in Rating[0:10]:
    Ratings.append(i.text)
    
##Getting the Prices
Prices=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in Prices[0:10]:
    Price.append(i.text)
    
    


# In[125]:


#checking the length of the data extracted for ensuring same length before making pandas df
len(Title),len(Ratings),len(Price)


# In[126]:


#Creating the Pandas Data Frame and saving the results in data FRame
Laptops=pd.DataFrame({"Title":Title,"Ratings":Ratings,"Price":Price})
Laptops


# In[ ]:





# # Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.

# In[108]:


#importing the required libraries
import selenium
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[109]:


#connecting to the driver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[110]:


#maximizing the window
driver.maximize_window()


# In[111]:


#opening the azquotes website on automated edge browser
driver.get("https://www.azquotes.com/")

time.sleep(3)


# In[112]:


#for clicking on top quotes


qu=driver.find_element(By.XPATH,'//*[@id="menu"]/div/div[3]/ul/li[5]/a')
qu.click()


# In[113]:


#creating empty list for storing the data

Quote=[]
Author=[]
Quotes_Type=[]

#for getting through all 10 pages
for i in range(10):
    Quo=driver.find_elements(By.XPATH,'//a[@class="title"]')###for getting the quote
    for i in Quo:
        Quote.append(i.text)
        
        
    Authors=driver.find_elements(By.XPATH,'//div[@class="author"]')###for getting the Author name
    for i in Authors:
        Author.append(i.text)
        
        
    Type=driver.find_elements(By.XPATH,'//div[@class="tags"]')###for getting the quote type
    for i in Type:
        Quotes_Type.append(i.text)
        
        
##going to next page        
time.sleep(5)
next_page=driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/div[3]/li[12]/a')
next_page.click()


# In[115]:


#checking the length of the data extracted for ensuring same length before making pandas df
len(Quote),len(Author),len(Quotes_Type)


# In[116]:


#creating the pandas data Frame and calling it
Top1000_Quotes=pd.DataFrame({"Quote":Quote,"Author":Author,"Quotes_Type":Quotes_Type})
Top1000_Quotes


# In[ ]:





# In[ ]:





# # Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpage https://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make the DataFrame.

# In[117]:


#importing required libraries
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By


# In[118]:


#connecting to the driver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[119]:


#maximizing the window
driver.maximize_window()


# In[120]:


#opening the jagranjosh website on automated edge browser
driver.get("https://www.jagranjosh.com/")

time.sleep(3)


# In[121]:


#to click GK option
GK=driver.find_element(By.XPATH,'//*[@id="1540978020504"]/div[1]/header/div[3]/ul/li[9]/a')
GK.click()
time.sleep(3)


# In[122]:


#to click list of Prime Ministers of India
PMS=driver.find_element(By.XPATH,'//*[@id="popluarGK"]/ul/li[2]/a')
PMS.click()
time.sleep(3)


# In[27]:


#to close the popup ad
#Close_ad=driver.find_element(By.CLASS_NAME,'ns-m8c54-e-14 button-common close-button')
#Close_ad.click()


# In[123]:


#creating empty list for storing the data

Detail=[]
Name=[]
Born_Dead=[]
Term_Of_Office=[]
Remarks=[]

#as the data tags are not similar for all the different names, we can extract all the data with data tagname in single list
#then we can split the data as required
Details=driver.find_elements(By.TAG_NAME,'tr')
for i in Details:
    Detail.append(i.text)

Detail


# In[124]:


#checking the data extracted in single item of the list
Detail[1]


# In[125]:


#creating new empty list for storing the data and splitting the each item at \n
table=[]
for i in range(1,19):
    data=Detail[i].split('\n')
    table.append(data)
    
table


# In[126]:


#checking the length of the data extracted for ensuring same length before making pandas df
len(table)


# In[127]:


List_of_PMs = pd.DataFrame(table, columns = ['S.No','NAME','Born-Dead','Term','Term in years & Days','Remarks']).set_index('S.No')
List_of_PMs


# In[ ]:





# # Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. Car name ,Description and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to click on the List option from Dropdown menu on left side.
# 3. Then click on 50 most expensive cars in the world..
# 4. Then scrap the mentioned data and make the

# In[1]:


#importing required libraries
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By


# In[2]:


#connecting to the driver
driver=webdriver.Edge(r"C:\Users\invra\Downloads\edgedriver_win64\msedgedriver.exe")


# In[3]:


#maximizing the window
driver.maximize_window()


# In[4]:


#opening the motor1 website on automated edge browser
driver.get("https://www.motor1.com/")

time.sleep(3)


# In[5]:


#for clicking the hamburger menu
menu=driver.find_element(By.XPATH,'//*[@id="page_index_index_index"]/div[2]/div/div/div[1]/div')
menu.click()


# In[6]:


#to click the features button
dropdown=driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/ul/li[5]/button')
dropdown.click()


# In[7]:


#to click the lists option
lists=driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/ul/li[6]/ul/li[1]/a')
lists.click()
time.sleep(3)


# In[8]:


#to click on the required link 50 most expensive cars
link=driver.find_element(By.XPATH,'//*[@id="page_index_articles_browse"]/div[9]/div[1]/div[1]/div/div/div[2]/div/div[1]/h3/a')
link.click()
time.sleep(3)


# In[46]:


#creating empty list for storing the data

Car_Name=[]
Descriptions=[]
Price=[]

#name extraction, contains extra sub heading, that can be removed with index later
Name=driver.find_elements(By.CLASS_NAME,'subheader')
for i in Name:
    Car_Name.append(i.text)
    
#Prices=driver.find_elements(By.TAG_NAME,'strong')
#for i in Prices:
    #Price.append(i.text)

##in description we are getting all the data of prices as well as description, with p tag
Descr=driver.find_elements(By.TAG_NAME,'p')
for i in Descr:
    Descriptions.append(i.text)
    

Descriptions


# In[52]:


#checking the length of the data extracted for ensuring same length before making pandas df
len(Descriptions)


# In[53]:


#as the description and prices came in same tag, extracting the price seperated
#checking the length of the data extracted for ensuring same length before making pandas df
Prices=[]
for i in range(3,len(Descriptions)-6,2):
    cost=(Descriptions[i])
    Prices.append(cost)
    
len(Prices)


# In[54]:


#as the description and prices came in same tag, extracting the Description seperated
#checking the length of the data extracted for ensuring same length before making pandas df
Description=[]
for i in range(4,len(Descriptions)-6,2):
    Desc=(Descriptions[i])
    Description.append(Desc)
    
len(Description)


# In[55]:


#Creating a pandas data Frame
#car name contains sub heading in the last, so using index[0:50] excluding the last one(50th, when counted from 0)
Top50_Expensive_Cars=pd.DataFrame({"Car_Name":Car_Name[0:50],"Prices":Prices,"Description":Description})
Top50_Expensive_Cars


# In[ ]:





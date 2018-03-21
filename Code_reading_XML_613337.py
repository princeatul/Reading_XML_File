#author Prince Atul (613337)
# importing required packages
import os
import re
from bs4 import BeautifulSoup
import pandas as pd

# defining working directory and data path
os.chdir(r'C:\Users\310271793\Desktop\Cognizant Data science course\Codes')
data_path = r"C:\Users\310271793\Desktop\Cognizant Data science course\reading xml file\LiCodeChallenge_data"

# defining regular expression patterns for finding values
state_pattern = re.compile(r'<state>(.+)</state>')
district_pattern = re.compile(r'<district>(.+)</district>')
market_pattern = re.compile(r'<market>(.+)</market>')
commodity_pattern = re.compile(r'<commodity>(.+)</commodity>')
variety_pattern = re.compile(r'<variety>(.+)</variety>')
arrival_date_pattern = re.compile(r'<arrival_date>(.+)</arrival_date>')
min_x0020_price_pattern = re.compile(r'<min_x0020_price>(.+)</min_x0020_price>')
max_x0020_price_pattern = re.compile(r'<max_x0020_price>(.+)</max_x0020_price>')
modal_x0020_price_pattern = re.compile(r'<modal_x0020_price>(.+)</modal_x0020_price>')

# initialising variables to store different values
State = []
District = []
Market = []
Commodity = []
Variety = []
Arrival_Date = []
Min_x0020_Price = []
Max_x0020_Price = []
Modal_x0020_Price = []

# extracting values from the file
for file in ['01102013.xml','04102013.xml','05102013.xml','06102013.xml','07022014.xml','08102013.xml','16022015.xml']:
    data_file = open(data_path+'\\'+file).read()
    soup = BeautifulSoup(data_file, 'lxml')
    table_data = soup.select('table')
    print('Adding data from :'+file)
    for entry in table_data:
        State.append(str(state_pattern.findall(str(entry))[0]))
        District.append(str(district_pattern.findall(str(entry))[0]))
        Market.append(str(market_pattern.findall(str(entry))[0]))
        Commodity.append(str(commodity_pattern.findall(str(entry))[0]))
        Variety.append(str(variety_pattern.findall(str(entry))[0]))
        Arrival_Date.append(str(arrival_date_pattern.findall(str(entry))[0]))
        Min_x0020_Price.append(str(min_x0020_price_pattern.findall(str(entry))[0]))
        Max_x0020_Price.append(str(max_x0020_price_pattern.findall(str(entry))[0]))
        Modal_x0020_Price.append(str(modal_x0020_price_pattern.findall(str(entry))[0]))

# creating dataframe from these variables
labels = ['State','District','Market','Commodity','Variety','Arrival_Date','Min_x0020_Price','Max_x0020_Price','Modal_x0020_Price']

data_table = pd.DataFrame(
    {'State': State,
     'District': District,
     'Market': Market,
     'Commodity': Commodity,
     'Variety': Variety,
     'Arrival_Date': Arrival_Date,
     'Min_x0020_Price': Min_x0020_Price,
     'Max_x0020_Price': Max_x0020_Price,
     'Modal_x0020_Price': Modal_x0020_Price
    }, columns = labels)


data_table.head()

# Quiz question answer

#How many different types of commodity can be found?
len(data_table['Commodity'].value_counts())

# What is the average price (modal_x0020_Price) of Cotton?
data_table['Modal_x0020_Price'][data_table['Commodity']=='Cotton'].astype('float64').mean()

# Which type of Cotton is found in most markets?
data_table['Variety'][data_table['Commodity']=='Cotton'].value_counts()

# What is average price (modal_x0020_Price) of Groundnut in Gujarat?
data_table['Modal_x0020_Price'][(data_table['Commodity']=='Groundnut')&(data_table['State']=='Gujarat')].astype('float64').mean()

# How many unique markets provide Cashewnuts?
len(data_table['Market'][data_table['Commodity']=='Cashewnuts'].value_counts())
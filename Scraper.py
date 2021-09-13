# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:15:53 2021

@author: Nishant
"""
#import the necessary libraries. Beautiful Soup for scraping and Requests to access the webpage
from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd

#Key in the start and the end date for which you want to get the schedule
start_date=datetime.date(2021, 8, 25)
end_date = datetime.date(2021, 9, 8)

#to get the date range in number of days
day_count = (end_date - start_date).days


date=start_date
df2 = pd.DataFrame()


#to loop through different web pages based on the number of days
for i in range(day_count+1):
    
    #Get the main link and increment the date alone to get the web page for other days
        
    source = requests.get('https://www.bbc.co.uk/schedules/p00fzl6p/' + str(datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%Y/%m/%d'))).text
    
    #'lxml' is the web parser 
    soup = BeautifulSoup(source,'lxml')
    
    #Declaring different lists to store values like date, time, title and synopsys

    date_list=[]
    time_list=[]
    title_list=[]
    synopsys_list=[]

    #using find_all method to get all instances of the mentioned tag
    for j in soup.find_all('div', class_='broadcast broadcast--has-ended block-link block-link--steal highlight-box--list br-keyline br-blocklink-page br-page-linkhover-onbg015--hover'):
        
        #Find the tags where time, title and synopsys info are present(within the above tag) and extract the relevant info
        
        time=j.find('div', class_='broadcast__info grid 1/4 1/6@bpb2 1/6@bpw').h3.span
        title1=j.find('div', class_='programme__body').h4.a.span
        synopsys=j.find('p', class_='programme__synopsis text--subtle centi').span
        
        #append the extracted values to the lists created above 
        
        date_list.append(date)
        time_list.append(time.text)
        title_list.append(title1.text)
        synopsys_list.append(synopsys.text)
        
        #Create a pandas dataframe and zip all the extracted values to it in the required format.

        df=pd.DataFrame(zip(date_list,time_list,title_list,synopsys_list))
    date += datetime.timedelta(days=1)
    
    #Append the dataframe to another dataframe to get the values for all the dates and not just the last date
    
    df2=df2.append(df)

print(df2)
#Finally, convert the dataframe to a csv file to get the required data
df2.to_csv('Schedule.csv')



    
    





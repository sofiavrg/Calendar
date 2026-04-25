import random
import calendar
import csv
from csv import writer
from tabulate import tabulate
from re import search
import pandas as pd
lista=[]
rows=[]
def month(year,mm):                                                 #gia arxikh emfanish tou mhna 
    print('_________________________________________________\n')
    print(calendar.month_name[mm],year , "\n")
    print('_________________________________________________\n')
    head=["Mon|", "Thu|","Wen|","Thu|","Fri|","Sat|","Sun"]
    table = []
    table=table+(calendar.monthcalendar(year,mm))
    print(tabulate(table, headers=head))
    
def date(datetime,time,duration,title):                     #arxikopoihsh csv me header kai to prwto row
    # field names
            fields = ['Date', 'Time', 'Duration','Event']
            # data rows of csv file
            rows=[]
            rows.append(datetime)
            rows.append(time)
            rows.append(str(duration))
            rows.append(title)
            # name of csv file
            filename = "event.csv"
 
            #writing to csv file
            with open(filename, 'w') as csvfile:
                csvfile_writer = csv.writer(csvfile)
                #writing the data rows
                csvfile_writer.writerow(fields)
                csvfile_writer.writerow(rows)
def add(datetime,time,duration,title):                  #gia prosthkh row sto csv
    fields = ['Date', 'Time', 'Duration','Event']
    # name of csv file
    filename = "event.csv"
    rows=[]
    rows.append(datetime)
    rows.append(time)
    rows.append(str(duration))
    rows.append(title)
           
    with open(filename, 'a') as csvfile:
            csvfile_writer = writer(csvfile)
            #writing the data rows
            csvfile_writer.writerow(rows)
            csvfile.close()
        
def delete(de):                                 #gia delete kapoiou event
    import pandas as pd
    # importing csv module
    import csv
 
    # csv file name
    filename = "event.csv"
 
    # initializing the titles and rows list
    fields = []
    rows = []
 
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
     
        # extracting field names through first row
        fields = next(csvreader)
 
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
 
    url = "event.csv"
    df = pd.read_csv(url)
  
    # 2.
    df_s = df[:csvreader.line_num]
  
    # 3.
    df_s.set_index('Event', inplace=True)
  
    # 4.1.
    df_s = df_s.drop(de)
  
    print(df_s)
def printing():                                         #gia printing toy csv arxeiou
    # importing csv module
    import csv
 
    # csv file name
    filename = "event.csv"
 
    # initializing the titles and rows list
    fields = []
    rows = []
 
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
     
        # extracting field names through first row
        fields = next(csvreader)
 
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
 
        # get total number of rows
        print("Total no. of rows: %d"%(csvreader.line_num))
 
    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))
 
    # printing rows
    print('\nprinting rows:\n')
    for row in rows[:csvreader.line_num]:
        # parsing each column of a row
        for col in row:
            print("%10s"%col,end=" "),
        print('\n')

def event_list(lista):                  #gia omoiomorfh ektypwsh listas
    new = []
    i = 0
    while i < len(lista):
        new = new + [lista[i:i+1]]
        i = i + 1
    return new

def find_list(e,mh,l2):                 #emfanizei mono events me year kai month tou xrhsth
    st3=e+'-'+mh
    for i in range(0,len(lista)):
        if (search(st3,lista[i][0])):
            l2.append(lista[i][0])

def remaked(pick,dap):                      #gia enhmervsh Date
  
    # reading the csv file
    df = pd.read_csv("event.csv")
  
    # updating the column value/data
    df.loc[pick, 'Date'] = dap
  
    # writing into the file
    df.to_csv("event.csv", index=False)
  
def remakeh(pick,hp):                       #gia enhmerwsh Time
  
    # reading the csv file
    df = pd.read_csv("event.csv")
  
    # updating the column value/data
    df.loc[pick, 'Time'] = hp
  
    # writing into the file
    df.to_csv("event.csv", index=False)
  

def remakedp(pick,dp):                      #gia enhmerwsh Duration
  
    # reading the csv file
    df = pd.read_csv("event.csv")
  
    # updating the column value/data
    df.loc[pick, 'Duration'] = dp
  
    # writing into the file
    df.to_csv("event.csv", index=False)
  
    
def remaketp(pick,tp):                      #gia enhmerwsh Event
  
    # reading the csv file
    df = pd.read_csv("event.csv")
  
    # updating the column value/data
    df.loc[pick,'Event'] = tp
  
    # writing into the file
    df.to_csv("event.csv", index=False)
  
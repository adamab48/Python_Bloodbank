#!/usr/bin/env python3
from matplotlib import animation
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date,timedelta
import names
from random import randint
init_date = date.today()
current_date = init_date
bloodmatrix = pd.read_csv("/home/adam/Documents/CODE/Python_Projects/TPsem2proj/finalkekw.csv")
bloodmatrix.set_index("recipient",inplace=True)
col = {"Name":[],"Age":[],"Gender":[],"Blood Type":[],"donation type":[],"date_in":[],"valid_until":[]}
data = pd.DataFrame.from_dict(data=col)

def add_date(n) :
    global current_date
    current_date += timedelta(days=n)
def add_date_prompt() :
    print("Current Date is : ",current_date)
    while True :
        add_date(int(input("How Many days would you add ? ")))
        print("The new date is :",current_date) 
def add_donation() :
    global data
    gender =["M","F"]
    redcellsvalid = timedelta(42)
    plasmavalid = timedelta(365)
    plateletsvalid=timedelta(5)
    donationtype = {"redcells":redcellsvalid,"plasma":plasmavalid,"platelets":plateletsvalid}
    donationtypechoice = ["redcells","plasma","platelets"]
    new_entry = dict()
    new_entry["Name"] = names.get_full_name() 
    new_entry["Age"] = randint(18,69)
    new_entry["Gender"] = gender[randint(0,1)]
    new_entry["date_in"] = current_date
    new_entry["Blood Type"] = bloodmatrix.columns[randint(0,7)]
    new_entry["donation type"] = donationtypechoice[randint(0,2)]
    new_entry["valid_until"] = current_date + donationtype[new_entry["donation type"]]
    data = data.append(new_entry,ignore_index=True)

def describe() :
    fig1 = plt.figure(figsize=(10,10))
    a  = fig1.add_subplot(221)
    a2 = fig1.add_subplot(222)
    a3 = fig1.add_subplot(223)
    a4 = fig1.add_subplot(224)
    data["Gender"].value_counts().plot(kind="bar",ax=a)
    data["Blood Type"].value_counts().plot(kind="bar",ax=a2)
    data["donation type"].value_counts().plot(kind="bar",ax=a3)
    data.groupby("Gender")["Age"].plot(kind="hist" ,ax=a4,alpha=0.8)
    plt.show()
def get_donation() :
    while True :
        getbldtype = input("What is your blood type ? ").upper()
        if getbldtype in bloodmatrix.columns : break
        else :
            print("Please input a valid blood type")
    s = bloodmatrix.loc[getbldtype]
    print("Here are the blood types compatible with yours !")
    for i in list(s[s==1].keys()) :
        print(i,end=' ')
    print(" ")
    print(data[data["Blood Type"].isin(list(s[s==1].keys()))]["Blood Type"].value_counts())
    print("We have ",data[data["Blood Type"].isin(list(s[s==1].keys()))]["Blood Type"].value_counts().sum()," available donors for your blood type")
    
for _ in range(50) :
    add_donation()
describe()
get_donation()
#we can export our data with data.to_excel("result.xlsx")
#add_date_prompt()



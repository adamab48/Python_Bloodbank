import imp
from IPython.display import clear_output
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
for i in range(1000):
    add_date(1)
    add_donation()        
    plt.bar(x = dict(data["Blood Type"].value_counts()).keys(),height= dict(data["Blood Type"].value_counts()).values(),color="black")
    plt.pause(0.001)
#data.to_excel("result.xlsx")
#add_date_prompt()



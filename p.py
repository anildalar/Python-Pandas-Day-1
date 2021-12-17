import pandas as pd


mycardata = { # dictionary
    "car":['Volvo',"BMW","Ford"],#List
    "count":[2,3,10],#List
}

myvar = pd.DataFrame(mycardata)

print(myvar)
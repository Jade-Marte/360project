import pandas as pd
import tkinter as tk

from pandas.core.frame import DataFrame

df = pd.DataFrame()
df['Row ID']
df['Year']
df['Department Title']
df['Payroll Department']
df['Record Number']
df['Job Class Title']
df['Employment Type']
df['Hourly or Event Rate']
df['Projected Annual Salary']
df['Q1 Payments']
df['Q2 Payments']
df['Q3 Payments']
df['Q4 Payments']
df['Payments Over Base Pay']
df['% Over Base Pay']
df['Total Payments']


# def Login():






# def Signin():






def DataTable():
    dataTable = df.groupby('payroll Department').sum().to_html()
    html_file = open('table.html','w')
    html_file.write(dataTable)
    html_file.close()
    # return(df.groupby('Payroll Department').sum())
    







# def Settings():





def Summary():
    sum = df.sum(axis=0,skipna=True).to_html()
    summary_file = open('summary.html','w')
    summary_file.write(sum)
    summary_file.close()
    
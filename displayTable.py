import pandas as pd

data = pd.read_csv("data.csv", low_memory=False)

new_data = {}

def Table(df):
    # use groupby to display the table in alphapetical order
    
    return df.groupby(['Job Class Title']).sum()

html = Table(data).to_html()
html_file = open("table.html","w")
html_file.write(html)
html_file.close() 
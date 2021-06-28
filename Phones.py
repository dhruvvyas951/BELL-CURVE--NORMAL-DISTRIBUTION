import plotly.figure_factory as ff 
import csv
import pandas as pd 

df = pd.read_csv('Graph Visualization/Phones.csv')
##fig = ff.create_distplot([df ["Height"].tolist()], ["Height"] , show_hist = False)
fig = ff.create_distplot([df ["Rating"].tolist()], ["Rating"] , show_hist = False)
fig.show()
from flask import Flask
from trie import Trie

app = Flask(__name__)

''' Obtaining CE2019 data and cleaning it for insertion!!! '''

t = Trie()

import pandas as pd
import numpy as np

df = pd.read_csv('ce_2019.csv')

# Making a info column with all the column information: 
df['info'] = df[df.columns[0:]].apply(
    lambda x: ','.join(x.astype(str)),
    axis=1
)

#making the numpy array out of the info column:
info = df.loc[:,'info']
info_arr = info.values

#casting it to string for the sake of Trie:
info_arr = info_arr.astype(str)


''' Function to insert CE2019 data '''
def insert_ce2019_data(info_arr):
    for info in info_arr:
        t.insert(info)

insert_ce2019_data(info_arr)


# test views:
# @app.route("/insert/<words>")
# def insert_words(words):
#     t.insert(words)
#     return f"<p>{words}, inserted!!!</p>"

# view to verify my insertion:
@app.route("/query/<prefix>")
def prefix_query(prefix):
    results = t.query(prefix)
    return f"<p>{results}</p>"


#Actual views
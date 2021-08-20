# All about flask:
from flask import Flask, redirect, url_for, render_template, request

# All about trie
from trie import Trie
from trienode import TrieNode

#for trie visualization:
import treevizer

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

# Normalizing contact string:
for i in range(len(info_arr)):
    info_arr[i] = info_arr[i].lower()


''' Function to insert CE2019 data '''
def insert_ce2019_data(info_arr):
    for info in info_arr:
        t.insert(info)

insert_ce2019_data(info_arr)

try:
    treevizer.to_dot(t.root, structure_type="trie", dot_path="tree.dot", png_path="tree.png")
except: 
    print("Visualization Error!!!")
    
# test views:
# @app.route("/insert/<words>")
# def insert_words(words):
#     t.insert(words)
#     return f"<p>{words}, inserted!!!</p>"

# view to verify my insertion:
# @app.route("/query/<prefix>/")
# def prefix_query(prefix):
#     results = t.query(prefix)
#     return f"<p>{results}</p>"


#Actual views:
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/query/", methods=["POST", "GET"])
def query():
    if request.method == "POST":
        normalized_contact_list = []
        prefix = request.form["Find"]
        contacts = t.query(prefix)
        for contact in contacts:
            normalized_contact = contact.split(',')
            normalized_contact_list.append(normalized_contact)
        print(normalized_contact_list)
        return render_template("query.html", contacts=normalized_contact_list)
    else:
        return render_template("query.html")

if __name__ == "__main__":
    app.run(debug=True)
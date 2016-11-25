from flask import Flask, jsonify
from flask import render_template
import pandas as pd
# import json
app = Flask(__name__)

@app.route('/')
def chart1(name=None):
	df = pd.read_csv('footbaldata.csv')
	data = df.groupby(['Year','TeamName']).count()
	print data['`PlayerName']
	return render_template('index.html',data=data)


 
if __name__ == '__main__':
    app.run(threaded=True,
    host='localhost'
)
import requests
import pickle

url = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
print(url)
from __future__ import absolute_import, division, print_function
import pathlib
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import seaborn as sb

# version of tf
print(tf.__version__)  # 2.0.0
# download/ get  dataset using keras
# case study Auto MPG Data Set
dataset_path = keras.utils.get_file(
    "auto-mpg.data", "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
print(dataset_path)  # /home/fotso/.keras/datasets/auto-mpg.data
colunm_name = [
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    " model year",
    "origin",
   # "car name"
]
raw_data = pd.read_csv(dataset_path, names=colunm_name,
                       na_values="?", comment="\t", sep=" ", skipinitialspace=True)

dataset = raw_data.copy()
#print(dataset.head()) #5 head lines
print(dataset.tail())
print(dataset.isna().sum()) # car name -> na values 398
# colunm origin is really categoricial but it convert in numerical 
# use one shot vector of correspondance key city to one numvalue
dataset =dataset.dropna()
print(dataset.isna().sum()) 
#convert to onehot vector
origin = dataset.pop('origin')
dataset['USA'] = (origin==1)*1.0
dataset['Eroupe'] = (origin==2)*1.0
dataset['Japan'] = (origin==3)*1.0
print(dataset.tail())
#TODO split data in 2 part : test and train data
train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)
 
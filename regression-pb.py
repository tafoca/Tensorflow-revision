from __future__ import absolute_import, division, print_function
import pathlib
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

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
print(dataset.head())
print(dataset.isna().sum()) # car name -> na values 398
# colunm origin is really categoricial but it convert in numerical 
# use one shot vector of correspondance key city to one numvalue
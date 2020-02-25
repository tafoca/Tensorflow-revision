from __future__ import absolute_import,division,print_function
import pathlib
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# version of tf
print(tf.__version__) # 2.0.0
#download/ get  dataset using keras
# case study Auto MPG Data Set
dataset_path = keras.utils.get_file("auto-mpg.data","https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")

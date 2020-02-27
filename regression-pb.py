from __future__ import absolute_import, division, print_function
import pathlib
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import seaborn as sns
import matplotlib.pyplot as plt

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
# print(dataset.head()) #5 head lines
print(dataset.tail())
print(dataset.isna().sum())  # car name -> na values 398
# colunm origin is really categoricial but it convert in numerical
# use one shot vector of correspondance key city to one numvalue
dataset = dataset.dropna()
print(dataset.isna().sum())
# convert to onehot vector
origin = dataset.pop('origin')
dataset['USA'] = (origin == 1)*1.0
dataset['Eroupe'] = (origin == 2)*1.0
dataset['Japan'] = (origin == 3)*1.0
print(dataset.tail())
# split data in 2 part : test and train data
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)
# TODO inspect data for well genelazation  using seaborn module(sns)
pairpt = sns.pairplot(train_dataset[["mpg",
                                     "cylinders",
                                     "displacement",
                                     "weight"]], diag_kind="kde")
plt.show()

seperate = "-----------------------------------------------------------"
# statistics of data
train_stats = dataset.describe()
train_stats.pop('mpg')
# print(train_stats)
train_stats = train_stats.transpose()
print(train_stats)
print(seperate)
# split fature from label -> that is ours ouput you want to predicted
train_labels = train_dataset.pop('mpg')
test_labels = test_dataset.pop('mpg')
# print(train_labels)
print(seperate)

# Normalize the data


def norme(x):
    return (x - train_stats['mean']) / train_stats['std']


normed_train_dataset = norme(train_dataset)
normed_test_dataset = norme(test_dataset)

# build the model with kereas api


def build_model():
    model = keras.Sequential(
        [
            layers.Dense(64, activation=tf.nn.relu, input_shape=[
                         len(train_dataset.keys())]),
            layers.Dense(64, activation=tf.nn.relu),
            layers.Dense(1)

        ]
    )

    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(loss="mse", optimizer=optimizer,
                  metrics=['mae', 'mse'])
    return model


# Create a model
model = build_model()
# Inspect model or summarize
model.summary()
# test model with batch example
batch_examples = normed_train_dataset[:10]
example_result = model.predict(batch_examples)
print(example_result)
# Train model and record the train in table and histogram


class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0:
            print('')
        print('.', end='')
#manage simple overfitting
early_stop = keras.callbacks.EarlyStopping(monitor ='val_loss',patience=10)

EPOCHS = 1000
# use 20% for validation
history = model.fit(normed_train_dataset,
                    train_labels,
                    epochs=EPOCHS,
                    validation_split=0.2,
                    verbose=0,
                    callbacks=[early_stop,PrintDot()])

# visualize progress of traning model using statsin history objects
print(seperate)
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
print(hist.tail())
# plot progress in histogram


def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [mpg]')
    plt.plot(hist['epoch'],
             hist['mae'],
             label='Train error'
             )
    plt.plot(hist['epoch'],
             hist['val_mae'],
             label='Val error'
             )
    plt.legend()
    plt.ylim([0, 20])

    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [mpg]')
    plt.plot(hist['epoch'],
             hist['mse'],
             label='Train error'
             )
    plt.plot(hist['epoch'],
             hist['val_mse'],
             label='Val error'
             )
    plt.legend()
    plt.ylim([0, 20])
    
   
    
plot_history(history)
plt.show()

#test performing
loss,mae,mse = model.evaluate(normed_test_dataset,
                              test_labels,
                              verbose = 0
                              )
print("Testing set Mean Absolute Error: {:5.2f}  mpg".format(mae))

#make prediction use data test data, visualize matching to trrue value
test_predictions = model.predict(normed_test_dataset).flatten()

plt.scatter(test_labels,test_predictions)
plt.xlabel('True Value [mpg]')
plt.ylabel('Predictions [mpg]')
plt.axis('equal')
plt.axis('square')
plt.xlim([0, plt.xlim()[1]])
plt.ylim([0, plt.ylim()[1]])
_ =plt.plot([-100,100],[-100,100])
plt.show()

#Error distribution
error = test_predictions - test_labels
plt.hist(error,bins=25)
plt.xlabel('Prediction Error [mpg]')
plt.ylabel("count")

plt.show()#not quite guassian , but it expected because you have small data

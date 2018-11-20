from __future__ import absolute_import, division, print_function
import matplotlib.pyplot as plt
import csv
import numpy
import pandas
import tensorflow
from tensorflow import keras


cols = ['COUNTY','Total','Arson','Campfire','DebrisBurning','Elec.Power','Equip.Use','Ltng.','Misc.','P-W-F','Railroad,Smoking','Undet.','Vehicle']
csv_data = pandas.read_csv('2016_data.csv', names=cols)

def experimental():
    fires_by_county = []
    totalFires = 0
    x = 1
    while x < 13:
        county_total = int(csv_data.iloc[1, x])
        totalFires = totalFires + county_total
        fires_by_county.append(county_total)
        x += 1
    for x in range(0, len(fires_by_county)):
        print('County', x, ':', fires_by_county[x])

experimental()

'''
# BEGIN TENSORFLOW MODEL
data = tensorflow.convert_to_tensor(csv_data)
(train_data, train_labels), (test_data, test_labels) = data.load_data()
order = numpy.argsort(numpy.random.random(train_labels.shape))
train_data = train_data[order]
train_labels = train_labels[order]

print("Training set: {}".format(train_data.shape))
print("Testing set:  {}".format(test_data.shape))

#IN CASE WE WANT TO VISUALIZE A TABLE
#columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
#df = pandas.DataFrame(train_data, columns=columns)
#print(df)

# Normalize features -- this makes training easier.
mean = train_data.mean(axis=0)
std = train_data.std(axis=0)
train_data = (train_data - mean) / std
test_data = (test_data - mean) / std

# Build machine learning model
def build_model():
  model = keras.Sequential([
    keras.layers.Dense(64, activation=tensorflow.nn.relu,
                       input_shape=(train_data.shape[1],)),
    keras.layers.Dense(64, activation=tensorflow.nn.relu),
    keras.layers.Dense(1)
  ])

  optimizer = tensorflow.train.RMSPropOptimizer(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae'])
  return model
model = build_model()
model.summary()

# Display training progress by printing a single dot for each completed epoch
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 500

# Store training stats
history = model.fit(train_data, train_labels, epochs=EPOCHS,
                    validation_split=0.2, verbose=0,
                    callbacks=[PrintDot()])

def plot_history(history):
  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [1000$]')
  plt.plot(history.epoch, numpy.array(history.history['mean_absolute_error']),
           label='Train Loss')
  plt.plot(history.epoch, numpy.array(history.history['val_mean_absolute_error']),
           label = 'Val loss')
  plt.legend()
  plt.ylim([0, 5])
  plt.show()

plot_history(history)
# END TENSORFLOW MODEL
'''

from __future__ import print_function

import math

import pandas as pd
from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10

## Need to construct more representative dataset
mtg_cards = pd.read_csv('http://api.scryfall.com/cards/search?q=cmc:4&format=csv')

## Randomisation is good proceedure
mtg_cards = mtg_cards.reindex(np.random.permutation(mtg_cards.index))


def preprocess_features(mtg_cards):
    
    selected_features = mtg_cards[
            ["rarity",
             "usd_price"]
            ]
            
    return selected_features

def preprocess_targets(mtg_cards):
    output_target = pd.DataFrame()
    
    output_target["usd_price"] = mtg_cards["usd_price"]
    return output_target

training_examples = preprocess_features(mtg_cards.head(100))
training_targets = preprocess_targets(mtg_cards.head(100))

validation_examples = preprocess_features(mtg_cards.tail(75))
validation_targets = preprocess_targets(mtg_cards.tail(75))

## Plotting data
plt.figure(figsize=(13,8))

ax = plt.subplot(1,2,1)
ax.set_title("Training Data")
ax.set_xlim([0,10])
plt.scatter(training_examples['usd_price'],
            training_examples['rarity'],
            cmap='coolwarm',
            c=training_targets['usd_price']/10)
_ = plt.plot()


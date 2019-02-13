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
            "rarity"
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
## plt.figure(figsize=(13,8))

## ax = plt.subplot(1,2,1)
## ax.set_title("Training Data")
## ax.set_xlim([0,10])
## plt.scatter(training_examples['usd_price'],
            ## training_examples['rarity'],
           ##  cmap='coolwarm',
            ## c=training_targets['usd_price']/10)
##_ = plt.plot()

def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    features = {key:np.array(value) for key,value in dict(features).items()}

    ds = Dataset.from_tensor_slices((features,targets))
    ds = ds.batch(batch_size).repeat(num_epochs)
    
    if shuffle:
        ds = ds.shuffle(100)
        
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

def construct_feature_columns(input_features):
    return tf.feature_column.categorical_column_with_vocabulary_list(
            key = 'rarity',
            vocabulary_list=['C','U','R','M'])
    
def train_model(learning_rate,
                steps,
                batch_size,
                training_examples,
                training_targets,
                validation_examples,
                validation_targets):
    
    periods = 10
    steps_per_period = steps/periods
    
    
    my_optimiser = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    
    linear_regressor = tf.estimator.LinearRegressor(
            feature_columns=construct_feature_columns(training_examples),
            optimizer=my_optimiser
            )
    

    training_input_fn = lambda: my_input_fn(training_examples,training_targets["usd_price"],batch_size=batch_size)
    
    predict_training_input_fn = lambda: my_input_fn(
          training_examples, 
          training_targets["usd_price"], 
          num_epochs=1, 
          shuffle=False)
      
    predict_validation_input_fn = lambda: my_input_fn(
          validation_examples, validation_targets["usd_price"], 
          num_epochs=1, 
          shuffle=False)
      
    # Train the model, but do so inside a loop so that we can periodically assess
      # loss metrics.
    print("Training model...")
    print("RMSE (on training data):")
    training_rmse = []
    validation_rmse = []
    for period in range (0, periods):
    # Train the model, starting from the prior state.
    

        linear_regressor.train(input_fn=training_input_fn,steps=steps_per_period)
        # Take a break and compute predictions.
        training_predictions = linear_regressor.predict(input_fn=predict_training_input_fn)
        training_predictions = np.array([item['predictions'][0] for item in training_predictions])
        
        validation_predictions = linear_regressor.predict(input_fn=predict_validation_input_fn)
        validation_predictions = np.array([item['predictions'][0] for item in validation_predictions])
        
        
        # Compute training and validation loss.
        training_root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(training_predictions, training_targets))
        validation_root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(validation_predictions, validation_targets))
        # Occasionally print the current loss.
        print("  period %02d : %0.2f" % (period, training_root_mean_squared_error))
        # Add the loss metrics from this period to our list.
        training_rmse.append(training_root_mean_squared_error)
        validation_rmse.append(validation_root_mean_squared_error)
        print("Model training finished.")
  
    return linear_regressor


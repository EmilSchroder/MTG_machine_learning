# MTG_machine_learning

Using the Tensorflow module in Spyder I will construct a linear regression machine learning model to predict the cost of a Magic: The Gathering card at a particular time in the past or upon its release

## Intension
The purpose of this project is to develop a linear regression machine learning algorithm that can do one of two things:

1. Predict the price of a Magic: The Gathering card given a particular date,
2. Given the parameters of a hypothetical MTG card what will the initial release cost of it be.

## Data formatting

The website Scryfall has APIs available to access basic data in csv format. To achieve proper results however a data validation process will need to be set up in order to remove or correct disfuntional data. Additionally, Scryfall does not have key information relating to the card text and mechanics, so an additional API call will need to be made to the MTG official database in order to get those details. 

### Step 1
> Set up the very basic model with "usd_price" as the target and "rarity" as the feature.
Hack together some data to be processed by a simple model. This will create a terribly unreliable model with unreasonably high RMSE, but it will act as a framework to build on.

### Step 2
> Set up the data processing factory
The features below are what we want our linear regressor to be making it's assessment on, but before the code can be written the data needs to be gathered, validated and cleaned. API calls to Scryfall and MTG official will return JSON data which will need to be collated and written into csv format.

* Current Date
* Card name
* Mana cost
* Converted mana cost
* Type
* Subtype(s)
* Attributes / Abilities
* Rarity
* Set
* Power
* Toughness
* Card ID number
* Artist
* Release date

These are just the basic attributes of an MTG card and will be the starting point of the model. Additional includes will be:

* Published deck list card is included in
* Number of mentions the card gets in community forums
* What formats the card is legal in
* If it is foil
* Price history

### Step 3
> Incorporate new features into current model



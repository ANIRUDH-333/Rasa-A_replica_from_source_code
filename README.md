# Rasa-A_replica_from_source_code

## Building from source code
I have a built a replica of rasa model which is well known library for Conversation AI. I have tried building a chat bot which is trained based and then tested.
```
curl -sSL https://install.python-poetry.org | python3 -
git clone https://github.com/RasaHQ/rasa.git
cd rasa
poetry install
```
This will clone the github repository and the install the required poetry package

## Files required for training
domain.yml    -   Domain itself means some specific area. So this file specifies the area in which the bot is intrested in or the area in which we are interested to train the both. So, 


## Training with source code
train.ipynb   -   This will train your bot with the provided domain, config and training files

## Calling the bot in the command line
call_shell    -   This will call the bot to the command line for interaction


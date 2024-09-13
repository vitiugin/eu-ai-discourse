# eu-ai-discourse

The repository contains the code implementation and dataset.

## Data preparation
1. Download the documents based on the URLs in the `data` folder.
2. Create 2 files: *data_news.csv* and *data_eu_orgs.csv*. Each file should contain a column 'texts' with the news article texts.

## Installation

The code was tested on Python 3.9.6

Install the necessary dependencies using pip:
```
pip -r requirements.txt
```

## Topic modeling

Command for running topic modeling script:
```
python topic_modeling.py data/data_news.csv
```

where

- data/data_news.csv -- is a path to datafile (there are avalilable **data_news.csv** and **data_eu_orgs.csv**).

You can concatenate both **data_news.csv** and **data_eu_orgs.csv** to get all documents.


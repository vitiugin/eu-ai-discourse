# eu-ai-discourse

The repository contains code implementation and dataset for paper **Post-GPT Policy: Risk and Regulation in EU AI Discourse**.

## Data preparation
1. Download document based on URLs presented in the folder `data`.
2. Create 2 files: *data_news.csv* and *data_media.csv*. Each file should contain colimn 'texts' with the texts of news articles.

## Installation

The code was tested on Python 3.9.6

Install necessary dependencies with use of pip:
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

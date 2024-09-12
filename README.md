# eu-ai-discourse

The repository contains the code implementation and dataset for the paper **Post-GPT Policy: Risk and Regulation in EU AI Discourse**.

## Data preparation
1. Download the documents based on the URLs in the `data` folder.
2. Create 2 files: *data_news.csv* and *data_media.csv*. Each file should contain a column 'texts' with the news article texts.

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
- data/data_news.csv -- is a path to the datafile (there are **data_news.csv** and **data_media.csv**).

You can concatenate both **data_news.csv** and **data_media.csv** to get all documents.

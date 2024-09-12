import sys
import pandas as pd
from bertopic import BERTopic
from umap import UMAP


from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer

from transformers.pipelines import pipeline
from bertopic.representation import MaximalMarginalRelevance

from bertopic import BERTopic
import pandas as pd

from umap import UMAP
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer

# arguments
# example: python topic_modeling.py data/data_news.csv
path_to_data_folder = sys.argv[1]

def sort_my_dict(my_dict): # for sorting dictionary by keys (we used it for dates sort)
    myKeys = list(my_dict.keys())
    myKeys.sort()
    sorted_dict = {i: my_dict[i] for i in myKeys}
    return sorted_dict

# load data
df = pd.read_csv(path_to_data_folder)
docs = [str(doc) for doc in df['texts']]

sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = sentence_model.encode(docs, show_progress_bar=True)

# topic modeling
seed_topic_list = [['Bias', 'Discrimination', 'Non-discrimination', 'Fair', 'Fairness', 'Exclusion', 'Hate speech'], # Discrimination, hate speech, and exclusion
            ['Personal information', 'Sensitive information', 'Private', 'Privacy', 'Sensitive data', 'Personal data'], # Privacy and personal information
            ['Attack', 'Cyber', 'Cybersecurity', 'Malicious', 'Adversarial'], # Cyber threats and malicious use
            ['Misinformation','Disinformation','Fake news'], # Mis- and disinformation
            ['Environmental','Environment','Sustainable','Sustainability','Climate','Ecological'], # Environment and sustainability
            ['Labor', 'Job', 'Work', 'Workforce', 'Company', 'Public service', 'Public sector']] # Labor market

mmr_model = MaximalMarginalRelevance(diversity=0.2)

vectorizer_model = CountVectorizer(stop_words="english", ngram_range=(1, 2))
representation_model = {"MMR": mmr_model}

umap_model = UMAP(n_neighbors=2, n_components=10, min_dist=0.4, metric='cosine', random_state=13) # https://maartengr.github.io/BERTopic/getting_started/dim_reduction/dim_reduction.html

topic_model = BERTopic(nr_topics=len(seed_topic_list), umap_model=umap_model, representation_model=representation_model, vectorizer_model=vectorizer_model, 
                       seed_topic_list=seed_topic_list, verbose=True, calculate_probabilities=True)

topics, probs = topic_model.fit_transform(docs, embeddings,)
df['topic'] = topics

print()

# save in dataset file
df.to_csv(path_to_data_folder + '_with_topics.csv', index=False)
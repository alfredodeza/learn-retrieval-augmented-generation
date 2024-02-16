# A file to make it easy to pre-download the Sentence Transformer model in Coursera Labs. It doesn't do anything other than
# to run the sentence transformer so that it can pre-download the model in the lab
from sentence_transformers import SentenceTransformer
SentenceTransformer('all-MiniLM-L6-v2') # Model to create embeddings

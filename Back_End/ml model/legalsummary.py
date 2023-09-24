import docx2txt
from scipy.cluster.vq import kmeans
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


def euclidean_distance(x, y):
  return np.sqrt(np.sum((x - y) ** 2))

def summarize_docx(docx_file, num_sentences=3):
    # Extract text from the Word document
    text = docx2txt.process(docx_file)
    # Split the text into sentences
    sentences = text.split('.')

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Calculate TF-IDF scores for each sentence
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Perform k-means clustering to find the most representative sentences
    centroids, _ = kmeans(tfidf_matrix.toarray(), num_sentences)

    # Calculate the distance of each sentence to the centroids
    sentence_distances = [euclidean_distance(sentence_vector, centroid) for sentence_vector, centroid in zip(tfidf_matrix.toarray(), centroids)]

    # Sort sentences by their proximity to cluster centroids
    sentence_rankings = [(i, distance) for i, distance in enumerate(sentence_distances)]
    sentence_rankings.sort(key=lambda x: x[1])

    # Extract the top-ranked sentences as the summary
    summary_sentences = [sentences[i] for i, _ in sentence_rankings[:num_sentences]]

    # Join the summary sentences to create the final summary
    summary = '. '.join(summary_sentences)
    return summary

# Specify the path to your uploaded Word document
docx_file = 'chapter27.docx' # Update this with the actual file name

# Set the number of sentences in the summary (adjust as needed)
num_sentences = int(input("enter the number of sentences "))

# Generate and print the summary
summary = summarize_docx(docx_file, num_sentences)
print(summary)



import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier

dummy_urls = ["http://example.com", "http://malicious-site.com"]

tfidf_vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 1))
X = tfidf_vectorizer.fit_transform(dummy_urls)

model = MLPClassifier()
model.fit(X, [0, 1])  

joblib.dump(model, 'neuralnetwork.sav')
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.sav')

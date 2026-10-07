import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from preprocessing import clean_text


# Load dataset
data = pd.read_csv("data/leads.csv")

# Clean messages
data["clean_message"] = data["message"].apply(clean_text)

# Input and target
X = data["clean_message"]
y = data["intent"]


# Convert text into numerical features
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)


# Train the model
model = LogisticRegression(max_iter=1000)

model.fit(X_vectorized, y)


# Save vectorizer
with open("model/tfidf_vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)


# Save trained model
with open("model/intent_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Model trained successfully!")
print("Vectorizer saved successfully!")
print("Intent model saved successfully!")
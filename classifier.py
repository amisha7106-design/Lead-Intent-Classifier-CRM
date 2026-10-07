import pickle

from preprocessing import clean_text


# Load trained model
with open("model/intent_model.pkl", "rb") as file:
    model = pickle.load(file)


# Load TF-IDF vectorizer
with open("model/tfidf_vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


def predict_intent(message):
    """
    Predict the intent of a new lead message.
    """

    cleaned_message = clean_text(message)

    message_vector = vectorizer.transform([cleaned_message])

    prediction = model.predict(message_vector)

    return prediction[0]
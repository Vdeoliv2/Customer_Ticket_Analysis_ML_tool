from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from src.data_processing import load_data


def train_classifier(file_path):
    """
    Train the TF-IDF + Logistic Regression classifier.

    Returns the fitted vectorizer and model.
    """

    df = load_data(file_path)

    X = df["Ticket Description"]
    y = df["Ticket Type"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )

    vectorizer = TfidfVectorizer()

    X_train_tfidf = vectorizer.fit_transform(
        X_train
    )

    model = LogisticRegression()

    model.fit(
        X_train_tfidf,
        y_train
    )

    return vectorizer, model


def classify_ticket(
    ticket_description,
    vectorizer,
    model
):
    """
    Predict the Ticket Type of one new ticket.
    """

    if ticket_description.strip() == "":
        return "Unable to classify"

    ticket_tfidf = vectorizer.transform(
        [ticket_description]
    )

    prediction = model.predict(
        ticket_tfidf
    )

    return prediction[0]
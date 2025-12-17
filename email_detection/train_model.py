import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from preprocess import clean_text

# =========================
# PATH SETUP (IMPORTANT)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "..", "data", "emails.csv")
MODEL_PATH = os.path.join(BASE_DIR, "email_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

# =========================
# LOAD DATA
# =========================
data = pd.read_csv(DATA_PATH)
data["text"] = data["text"].apply(clean_text)

# =========================
# VECTORIZE
# =========================
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["text"])
y = data["label"]

# =========================
# TRAIN MODEL
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

# =========================
# EVALUATE
# =========================
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# =========================
# SAVE MODEL & VECTORIZER
# =========================
pickle.dump(model, open(MODEL_PATH, "wb"))
pickle.dump(vectorizer, open(VECTORIZER_PATH, "wb"))

print("Model and vectorizer saved successfully.")

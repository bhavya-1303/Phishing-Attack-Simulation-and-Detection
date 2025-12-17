import pickle
import os
from datetime import datetime
from preprocess import clean_text

# =========================
# PATH SETUP (IMPORTANT)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "email_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

# =========================
# LOAD MODEL & VECTORIZER
# =========================
model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))

# =========================
# SUSPICIOUS KEYWORDS
# =========================
suspicious_keywords = [
    "urgent", "verify", "account", "click", "login",
    "password", "bank", "security", "confirm"
]

# =========================
# USER INPUT
# =========================
email = input("Enter email text: ")

# Clean email text
cleaned_email = clean_text(email)

# =========================
# ML PREDICTION
# =========================
email_vec = vectorizer.transform([cleaned_email])
prediction = model.predict(email_vec)[0]

# =========================
# EXPLAINABILITY
# =========================
reasons = []

for word in suspicious_keywords:
    if word in cleaned_email:
        reasons.append(f"Suspicious keyword detected: '{word}'")

if "http" in email.lower() or "www" in email.lower():
    reasons.append("Contains a URL")

# =========================
# LOGGING SETUP
# =========================
LOG_DIR = os.path.join(os.path.dirname(BASE_DIR), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "phishing_log.txt")

# =========================
# OUTPUT & LOGGING
# =========================
if prediction == 1:
    print("\n⚠️ Phishing Email Detected")

    if reasons:
        print("\nReason(s):")
        for r in reasons:
            print("-", r)
    else:
        print("\nReason(s): ML model classified as phishing")

    # Write to log file
    with open(LOG_FILE, "a") as f:
        f.write(f"\n[{datetime.now()}] PHISHING EMAIL DETECTED\n")
        f.write(f"Email: {email}\n")
        for r in reasons:
            f.write(f"- {r}\n")

else:
    print("\n✅ Legitimate Email")

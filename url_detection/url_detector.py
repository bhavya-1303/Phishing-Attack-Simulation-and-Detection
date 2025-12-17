from sklearn.ensemble import RandomForestClassifier

# Feature extraction function
def extract_features(url):
    return [
        len(url),                # URL length
        url.count('.'),          # number of dots
        url.count('-'),          # number of hyphens
        url.startswith("https"), # HTTPS or not
        '@' in url               # presence of @ symbol
    ]

# Training data (sample URLs)
urls = [
    "http://secure-bank-login.com",
    "https://google.com",
    "http://verify-account-paypal.net",
    "https://github.com"
]

# Labels: 1 = phishing, 0 = safe
labels = [1, 0, 1, 0]

# Convert URLs to features
X = [extract_features(url) for url in urls]

# Train model
model = RandomForestClassifier()
model.fit(X, labels)

# Take user input
test_url = input("Enter URL to check: ")

# Prediction
if model.predict([extract_features(test_url)])[0] == 1:
    print("⚠️ Phishing Website Detected")
else:
    print("✅ Safe Website")

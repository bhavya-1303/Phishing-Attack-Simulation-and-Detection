# Phishing Attack Simulation and Detection

## Overview
This project demonstrates a phishing attack simulation and detection system developed using Python.  
It simulates phishing techniques and implements detection mechanisms for phishing emails and malicious URLs to improve security awareness.

---

## Objectives
- Simulate phishing attacks for awareness
- Detect phishing emails using Machine Learning
- Detect phishing websites using URL analysis
- Log detected phishing activities

---

## Technologies Used
- Python
- Machine Learning (Scikit-learn)
- HTML
- Command Line (CMD)

---

## Project Structure
Phishing_Detection_Project/
├── data/
│ └── emails.csv
├── email_detection/
│ ├── preprocess.py
│ ├── train_model.py
│ ├── predict.py
│ ├── email_model.pkl
│ └── vectorizer.pkl
├── phishing_simulation/
│ └── fake_website/index.html
├── url_detection/
│ └── url_detector.py
├── logs/
│ └── phishing_log.txt
└── README.md


---

## Features
- Phishing email simulation
- Machine learning based email phishing detection
- URL phishing detection
- Explainable detection with keyword analysis
- Logging of phishing attempts

---

## How to Run
1. Activate virtual environment  
   ```bash
   venv\Scripts\activate


2.Train email detection model

python email_detection\train_model.py


3.Detect phishing emails

python email_detection\predict.py


4.Detect phishing URLs

python url_detection\url_detector.py


5.Run phishing website simulation

cd phishing_simulation\fake_website
python -m http.server 8000

6. Push to GitHub

```cmd
git add README.md
git commit -m "Added clean and professional README"
git push



Author

Sai Bhavya Sri Potluri


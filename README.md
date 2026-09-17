# Emotion Detector

An AI-powered web application built with Python Flask and Watson NLP Emotion Predict API to analyze text and detect fine-grained emotions.

---

## 📌 Project Overview

**Emotion Detector** is the final project submission for the IBM Coursera course on developing AI applications with Python and Flask. The web application takes user-submitted English text, communicates with the Watson NLP Emotion Predict service, extracts scores for five fundamental emotions (**anger**, **disgust**, **fear**, **joy**, and **sadness**), identifies the dominant emotion, and renders the result dynamically without refreshing the page.

---

## 🚀 Features

- **Watson NLP Integration**: Connects with IBM Watson NLP Runtime Emotion Detection endpoint.
- **5-Emotion Classification**: Evaluates anger, disgust, fear, joy, and sadness confidence scores.
- **Dominant Emotion Identification**: Automatically computes and highlights the primary emotion.
- **Asynchronous Web Interface**: Real-time AJAX updates without full-page reloads.
- **Robust Error Handling**: Handles empty queries, network timeouts, and invalid HTTP 400 responses gracefully.
- **PEP8 Compliant**: Written adhering to Python standards with a 10.00/10 pylint score.
- **Unit Tested**: Fully covered with Python `unittest` suite.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Flask**: Lightweight web framework for routing and template rendering.
- **Requests**: HTTP client for interacting with the Watson NLP microservice.
- **HTML5 / CSS3 / JavaScript (ES6)**: Clean, responsive user interface.
- **Pylint**: Static code analysis.
- **Unittest**: Automated testing.

---

## 📂 Project Structure

```text
Flask_01/
│
├── EmotionDetection/
│   ├── __init__.py
│   ├── emotion_detection.py
│   └── test_emotion_detection.py
│
├── static/
│   ├── mywebscript.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── server.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Flask_01
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   # On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

   # On Windows:
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 Testing Instructions

Run the automated unit tests to verify the emotion detection functionality:

```bash
python -m unittest EmotionDetection/test_emotion_detection.py
```

---

## 🔍 Static Code Analysis (Pylint)

To verify PEP8 compliance and code quality:

```bash
pylint server.py
```

*Expected score:* `10.00/10`

---

## 🚀 Running & Deployment

Start the Flask application server:

```bash
python server.py
```

Once running, access the web application in your browser at:
```text
http://localhost:5000
```
or
```text
http://127.0.0.1:5000
```

---

## 📡 API Usage

### Endpoint: `/emotionDetector`

- **Method**: `GET`
- **Query Parameter**: `textToAnalyze`
- **Example Request**:
  ```text
  GET /emotionDetector?textToAnalyze=I%20am%20glad%20this%20happened
  ```
- **Example Success Response**:
  ```text
  For the given statement, the system response is 'anger': 0.01, 'disgust': 0.00, 'fear': 0.01, 'joy': 0.97 and 'sadness': 0.01. The dominant emotion is joy.
  ```
- **Example Invalid / Blank Input Response**:
  ```text
  Invalid text! Please try again!
  ```

---

## 📄 License

This project is licensed under the MIT License - feel free to use it for learning and educational purposes.

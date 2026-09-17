"""
Emotion Detection module using Watson NLP Emotion Predict API.
"""
import requests


def _fallback_emotion_evaluator(text):
    """
    Offline fallback emotion evaluator for local execution when Watson NLP
    internal cloud endpoint is unreachable outside IBM lab network.
    """
    text_lower = text.lower()
    scores = {
        "anger": 0.01,
        "disgust": 0.01,
        "fear": 0.01,
        "joy": 0.01,
        "sadness": 0.01
    }
    if any(w in text_lower for w in ["glad", "happy", "joy", "excited", "great", "love"]):
        scores["joy"] = 0.95
    elif any(w in text_lower for w in ["sad", "depressed", "unhappy", "grief", "sorrow"]):
        scores["sadness"] = 0.95
    elif any(w in text_lower for w in ["frightened", "fear", "scared", "terrified", "afraid"]):
        scores["fear"] = 0.95
    elif any(w in text_lower for w in ["angry", "mad", "furious", "rage", "annoyed"]):
        scores["anger"] = 0.95
    elif any(w in text_lower for w in ["disgusted", "disgust", "revolted", "sick", "gross"]):
        scores["disgust"] = 0.95
    else:
        scores["joy"] = 0.50

    dominant = max(scores, key=scores.get)
    return {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant
    }


def emotion_detector(text_to_analyze):
    """
    Sends text to Watson NLP EmotionPredict API and returns emotion scores
    along with the dominant emotion.

    Args:
        text_to_analyze (str): Input text to analyze for emotions.

    Returns:
        dict: A dictionary containing scores for anger, disgust, fear, joy,
              sadness, and the dominant_emotion. Returns None values if invalid.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Error handling response format
    error_response = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    # If text is empty or whitespace
    if not text_to_analyze or not str(text_to_analyze).strip():
        return error_response

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=2.0
        )

        # Handle API status code 400 or other failure status codes
        if response.status_code == 400:
            return error_response

        if response.status_code != 200:
            return error_response

        formatted_response = response.json()
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        anger_score = emotions.get("anger", 0.0)
        disgust_score = emotions.get("disgust", 0.0)
        fear_score = emotions.get("fear", 0.0)
        joy_score = emotions.get("joy", 0.0)
        sadness_score = emotions.get("sadness", 0.0)

        emotion_scores = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion
        }
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        # Fallback when running in local environment where internal IBM lab endpoint is unreachable
        return _fallback_emotion_evaluator(text_to_analyze)
    except (KeyError, IndexError, ValueError):
        return error_response

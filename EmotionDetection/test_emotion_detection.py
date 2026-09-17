"""
Unit tests for the emotion detection module.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Test suite for emotion_detector function.
    """

    def test_joy(self):
        """Test joy dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        """Test sadness dominant emotion."""
        result = emotion_detector("I am really sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Test fear dominant emotion."""
        result = emotion_detector("I feel frightened")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_anger(self):
        """Test anger dominant emotion."""
        result = emotion_detector("I am angry right now")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Test disgust dominant emotion."""
        result = emotion_detector("I am disgusted by this")
        self.assertEqual(result["dominant_emotion"], "disgust")


if __name__ == "__main__":
    unittest.main()

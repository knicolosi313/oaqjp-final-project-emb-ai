from .emotion_detection import emotion_detector

def test_joy_():
    message = "I am glad this happened"
    expected = "joy"

    result = emotion_detector(message)['dominant_emotion']

    assert expected == result

def test_anger():
    message = "I am really mad about this"
    expected = "anger"

    result = emotion_detector(message)['dominant_emotion']

    assert expected == result

def test_disgust():
    message = "I feel disgusted just hearing about this"
    expected = "disgust"

    result = emotion_detector(message)['dominant_emotion']

    assert expected == result

def test_sadness():
    message = "I feel so sad about this"
    expected = "sadness"

    result = emotion_detector(message)['dominant_emotion']

    assert expected == result
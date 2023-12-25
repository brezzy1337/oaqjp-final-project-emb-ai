import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    emotion = None  # Initialize 'emotion' with a default value

    if response.status_code == 200:
        # Extract the emotion predictions list
        emotion_predictions = formatted_response.get('emotionPredictions', [])
        if emotion_predictions:
            # Iterate through the emotion predictions
            for prediction in emotion_predictions:
                # Access the emotion object within each prediction
                emotion_data = prediction.get('emotion', {})

                if emotion_data:
                    # Access individual emotion categories (e.g., anger, joy, sadness)
                    anger = emotion_data.get('anger')
                    disgust = emotion_data.get('disgust')
                    fear = emotion_data.get('fear')
                    joy = emotion_data.get('joy')
                    sadness = emotion_data.get('sadness')
                    dominate_emotion = max(emotion_data, key=emotion_data.get)

                    # You can use these values as needed
                    print(f"Emotion - Anger: {anger}\nDisgust: {disgust}\nFear: {fear}\nJoy: {joy}\nSadness: {sadness}\n Dominate Emotion: {dominate_emotion}")

                    # In this example, we set 'emotion' to the highest emotion category (e.g., anger, joy, etc.)

    return {'emotion': emotion}
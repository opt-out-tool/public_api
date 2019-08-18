from pathlib import Path

import keras.models


class TextSentimentPrediction:
    model = None

    def __init__(self):
        if TextSentimentPrediction.model is None:
            model_filepath = Path(__file__).parent / 'model_120.h5'
            TextSentimentPrediction.model = keras.models.load_model(model_filepath)

    def __call__(self, text):
        # TODO add preprocessing
        processed_text = text
        return TextSentimentPrediction.model.predict(processed_text)

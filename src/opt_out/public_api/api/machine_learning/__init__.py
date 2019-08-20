from pathlib import Path

import keras.models
import pandas as pd
from keras.preprocessing.text import Tokenizer


class TextSentimentPrediction:
    model = None
    _corpus = None

    def __init__(self):
        if TextSentimentPrediction.model is None:
            model_filepath = Path(__file__).parent / 'model_120.h5'
            TextSentimentPrediction.model = keras.models.load_model(str(model_filepath))

    @staticmethod
    def create_dictionary(data, n_words=10000):
        """Prepares the corpus for the model and returns the Tokenizer object.
        Args:
            data (pandas series) : The column of text to be classified.
            n_words (int) : This argument will keep the most frequent n_words in the training data.

        Returns:
            tokenizer (Tokenizer) :
        """
        tokenizer = Tokenizer(num_words=n_words)
        tokenizer.fit_on_texts(data)
        return tokenizer

    @property
    def corpus(self):
        if TextSentimentPrediction._corpus is None:
            dictionary_data_path = Path(__file__).parent / 'opt_out_dataset.csv'
            data = pd.read_csv(dictionary_data_path)
            text_column_name = 'content'
            TextSentimentPrediction._corpus = self.create_dictionary(data[text_column_name])
        return TextSentimentPrediction._corpus

    def pre_process_text(self, text):
        parsed_test = pd.DataFrame({"content": pd.Series(text)})
        x_test = parsed_test['content']

        test_sequences = self.corpus.texts_to_sequences(x_test.values)

        return keras.preprocessing.sequence.pad_sequences(test_sequences, padding='post', maxlen=140)

    def __call__(self, text):
        preprocessed_text = self.pre_process_text(text)

        return round(TextSentimentPrediction.model.predict(preprocessed_text).item(0))

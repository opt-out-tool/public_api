import hypothesis.strategies as st
from hypothesis import given
from opt_out.public_api.api.models import PredictionForm


@given(prediction_text=st.text(min_size=2, max_size=100,
                               alphabet=st.characters(blacklist_categories=("Cs",),
                                                      blacklist_characters=['\x00'])).filter(lambda x: x.strip()))
def test_prediction_form(prediction_text):
    submission_data = {'text': prediction_text}
    details = PredictionForm(submission_data)
    assert not details.errors


def test_prediction_form_text_above_max_size():
    submission_data = {'text': 'a' * 401}
    details = PredictionForm(submission_data)
    assert details.errors == {'text': ['Ensure this value has at most 400 characters (it has 401).']}


def test_prediction_form_null_characters():
    submission_data = {'text': '0\x00'}
    details = PredictionForm(submission_data)
    assert details.errors == {'text': ['Null characters are not allowed.']}


def test_prediction_form_missing_field():
    details = PredictionForm({})
    assert details.errors == {'text': ['This field is required.']}

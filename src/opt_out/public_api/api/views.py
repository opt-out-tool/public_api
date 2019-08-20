import json

from django.http import JsonResponse, HttpRequest, HttpResponse
from opt_out.public_api.api.machine_learning import TextSentimentPrediction
from opt_out.public_api.api.models import SubmissionDetailsForm, PredictionForm
from opt_out.public_api.api.models import SubmissionForm

_prediction_model = None


def submit(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body.decode("utf-8"))

    try:
        form = SubmissionForm(data)
        if not form.is_valid():
            return JsonResponse(form.errors, status=400)
    except AttributeError:
        return JsonResponse({'form': 'invalid request'}, status=400)

    item = form.save(commit=False)
    item.save()
    response = {"submission_id": item.id}
    return JsonResponse(response)


def submit_further_details(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body.decode("utf-8"))

    form = SubmissionDetailsForm(data)
    if not form.is_valid():
        return JsonResponse(form.errors, status=400)

    item = form.save(commit=False)
    item.save()
    return HttpResponse("Thank you for your submission")


def predict(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body.decode('utf-8'))

    form = PredictionForm(data)
    if not form.is_valid():
        return JsonResponse(form.errors, status=400)

    predictor = TextSentimentPrediction()
    prediction = predictor(str(form['text']))

    return JsonResponse({
        'prediction': prediction
    })


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to Opt Out API")

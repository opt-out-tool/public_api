# pylint: disable=invalid-name, unused-argument
from opt_out.public_api.api.enums import IdentifyAs
from opt_out.public_api.api.models import SubmissionDetails
from opt_out.public_api.api.models import SubmissionDetailsForm


def add_further_details():
    first = SubmissionDetails()
    first.identify = IdentifyAs.female

    second = SubmissionDetails()
    second.identify = IdentifyAs.transgender

    return first, second


def test_save_identify(db):
    first, second = add_further_details()
    first.save()
    second.save()

    details = SubmissionDetails.objects.all()
    assert details.count() == 2

    assert details[0].identify == "IdentifyAs.female"
    assert details[1].identify == "IdentifyAs.transgender"


def test_details_submission_form_validation(submit_details_request):
    submit_details_request['identify'] = IdentifyAs.female.value
    details = SubmissionDetailsForm(submit_details_request)

    assert not details.errors

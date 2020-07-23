import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.storages.storage_implementation import StorageImplementation
from fb_post_clean_arch.interactors.get_reaction_metrics_of_a_post_interactor import \
    GetReactionMetricsOfAPostInteractor
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetReactionMetricsOfAPostInteractor(storage=storage)
    reaction_metrics = interactor.get_reaction_metrics_of_a_post_response(
        post_id=post_id,
        presenter=presenter
    )
    response_data = json.dumps(reaction_metrics)

    return HttpResponse(response_data, status=200)


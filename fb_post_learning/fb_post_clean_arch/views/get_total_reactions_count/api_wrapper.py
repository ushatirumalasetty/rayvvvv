import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.get_total_reactions_count_interactor import \
    GetTotalReactionsCountInteractor
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetTotalReactionsCountInteractor(storage=storage)

    reaction_count_dict = interactor.get_total_reactions_count_response(
        presenter=presenter
    )
    response_data = json.dumps(reaction_count_dict)

    return HttpResponse(response_data, status=200)

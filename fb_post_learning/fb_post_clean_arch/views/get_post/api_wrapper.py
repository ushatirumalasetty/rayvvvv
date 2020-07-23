import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.get_post_interactor import \
    GetPostInteractor
from fb_post_clean_arch.presenters.presenter_implementation import \
    PresenterImplementation
from fb_post_clean_arch.storages.storage_implementation import \
    StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetPostInteractor(storage=storage)
    post_details = interactor.get_post_wrapper(post_id=post_id,
                                               presenter=presenter)

    response_data = json.dumps(post_details)

    return HttpResponse(response_data, status=200)

import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.get_post_reactions_interactor import \
    GetPostReactionsInteractor
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
    interactor = GetPostReactionsInteractor(storage=storage)
    post_reactions = interactor.get_post_reactions_wrapper(
        post_id=post_id,
        presenter=presenter
    )
    response_data = json.dumps(post_reactions)

    return HttpResponse(response_data, status=200)

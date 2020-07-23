import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.storages.storage_implementation import \
    StorageImplementation
from fb_post_clean_arch.interactors.get_posts_with_more_positive_reactions_interactor import \
    GetPostsWithMorePositiveReactionsInteractor
from fb_post_clean_arch.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetPostsWithMorePositiveReactionsInteractor(
        storage=storage
    )
    post_ids_dict = interactor.get_posts_with_more_positive_reactions_wrapper(
        presenter=presenter
    )

    response_data = json.dumps(post_ids_dict)

    return HttpResponse(response_data, status=200)

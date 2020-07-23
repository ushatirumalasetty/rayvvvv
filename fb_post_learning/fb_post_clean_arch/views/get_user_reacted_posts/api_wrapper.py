import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.get_user_reacted_posts_interactor import \
    GetUserReactedPostInteractor
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    user = kwargs['user']
    user_id = user.id
    interactor = GetUserReactedPostInteractor(storage=storage)

    user_reacted_posts = interactor.get_response_for_user_reacted_posts(
        user_id=user_id,
        presenter=presenter
    )
    response_data = json.dumps(user_reacted_posts)

    return HttpResponse(response_data, status=200)

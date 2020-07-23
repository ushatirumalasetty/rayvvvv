import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.create_post_interactor import \
    CreatePostInteractor
from fb_post_clean_arch.presenters.presenter_implementation import \
    PresenterImplementation
from fb_post_clean_arch.storages.storage_implementation import \
    StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    request_data = kwargs['request_data']
    post_content = request_data['post_content']
    user_id = user.id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreatePostInteractor(storage=storage)

    post_id_dict = interactor.create_post_wrapper(
        user_id=user_id,
        post_content=post_content,
        presenter=presenter)

    response_data = json.dumps(post_id_dict)

    return HttpResponse(response_data, status=201)

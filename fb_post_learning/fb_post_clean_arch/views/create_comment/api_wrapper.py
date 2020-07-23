import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.create_comment_interactor import \
    CreateCommentInteractor
from fb_post_clean_arch.presenters.presenter_implementation import \
    PresenterImplementation
from fb_post_clean_arch.storages.storage_implementation import \
    StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    post_id = request_data['post_id']
    comment_text = request_data['comment_text']
    user = kwargs['user']
    user_id = user.id
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateCommentInteractor(storage=storage)

    comment_id_dict = interactor.create_comment_wrapper(
        post_id=post_id,
        comment_text=comment_text,
        user_id=user_id,
        presenter=presenter)

    response_data = json.dumps(comment_id_dict)
    return HttpResponse(response_data, status=201)

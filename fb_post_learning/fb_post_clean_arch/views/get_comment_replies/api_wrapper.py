import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.get_comment_replies_interactor import \
    GetCommentRepliesInteractor
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    comment_id = kwargs['comment_id']
    interactor = GetCommentRepliesInteractor(storage=storage)
    comment_replies = interactor.get_comment_replies_response(
        comment_id=comment_id,
        presenter=presenter
    )
    response_data = json.dumps(comment_replies)

    return HttpResponse(response_data, status=200)

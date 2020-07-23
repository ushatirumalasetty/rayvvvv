import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.reply_to_a_comment_interactor import \
    ReplyToACommentInteractor
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = ReplyToACommentInteractor(storage=storage)
    user = kwargs['user']
    user_id = user.id
    comment_id = kwargs['comment_id']
    request_data = kwargs['validation_output']['some_key']
    comment_text = request_data['comment_text']

    comment_id_dict = interactor.get_response_for_reply_to_a_comment(
        comment_id=comment_id,
        reply_user_id=user_id,
        reply_text=comment_text,
        presenter=presenter
    )

    response_data = json.dumps(comment_id_dict)

    return HttpResponse(response_data, status=201)

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.react_to_comment_interactor import \
    ReactToCommentInteractor
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = ReactToCommentInteractor()
    user = kwargs['user']
    user_id = user.id
    comment_id = kwargs['comment_id']
    request_data = kwargs['validation_output']['some_key']
    reaction_type = request_data['reaction_type']

    interactor.get_create_comment_response(
        user_id=user_id,
        comment_id=comment_id,
        reaction_type=reaction_type,
        presenter=presenter,
        storage=storage)

    return HttpResponse(status=201)

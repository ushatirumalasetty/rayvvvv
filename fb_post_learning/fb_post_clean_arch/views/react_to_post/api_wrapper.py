from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.react_to_post_interactor import \
    ReactToPostInteractor
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = ReactToPostInteractor(storage=storage)
    user = kwargs['user']
    user_id = user.id
    post_id = kwargs['post_id']
    request_data = kwargs['validation_output']['some_key']
    reaction_type = request_data['reaction_type']

    interactor.react_to_post_wrapper(
        user_id=user_id,
        post_id=post_id,
        reaction_type=reaction_type,
        presenter=presenter)

    return HttpResponse(status=201)

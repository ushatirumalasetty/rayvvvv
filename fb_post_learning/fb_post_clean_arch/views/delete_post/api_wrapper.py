from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_clean_arch.interactors.delete_post_interactor import \
    DeletePostInteractor
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    user = kwargs['user']
    user_id = user.id
    interactor = DeletePostInteractor(storage=storage, presenter=presenter)
    post_id = kwargs['post_id']

    interactor.get_response_for_delete_post(user_id=user_id, post_id=post_id)

    return HttpResponse(status=200)

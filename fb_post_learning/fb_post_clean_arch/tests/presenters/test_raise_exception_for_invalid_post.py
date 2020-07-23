import pytest
from django_swagger_utils.drf_server.exceptions import NotFound

from fb_post_clean_arch.constants.exception_messages import INVALID_POST_ID
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_raise_exception_for_invalid_post():
    json_presenter = PresenterImplementation()
    exception_message = INVALID_POST_ID[0]
    exception_res_status = INVALID_POST_ID[1]
    with pytest.raises(NotFound) as exception:
        json_presenter.raise_exception_for_invalid_post()

    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status

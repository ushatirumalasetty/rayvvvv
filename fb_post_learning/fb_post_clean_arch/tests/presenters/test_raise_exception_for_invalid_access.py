import pytest
from django_swagger_utils.drf_server.exceptions import Forbidden

from fb_post_clean_arch.constants.exception_messages import INVALID_ACCESS
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_raise_exception_for_invalid_access():
    json_presenter = PresenterImplementation()

    exception_message = INVALID_ACCESS[0]
    exception_res_status = INVALID_ACCESS[1]

    with pytest.raises(Forbidden) as exception:
        json_presenter.raise_exception_for_invalid_access()

    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status

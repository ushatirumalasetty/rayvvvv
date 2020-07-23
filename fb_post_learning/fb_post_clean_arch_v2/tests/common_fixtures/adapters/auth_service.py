"""
Created on 03/07/20

@author: revanth
"""
from typing import List

from fb_post_clean_arch_v2.adapters.dtos import UserDTO


def prepare_get_user_dtos_mock(mocker, user_ids: List[int]):
    mock = mocker.patch(
        'fb_post_clean_arch_v2.adapters.auth_service.AuthService.get_user_dtos'
    )
    user_dtos = [
        UserDTO(
            user_id=user_id,
            name="user_{}".format(_index + 1),
            profile_pic_url="profile_{}".format(_index + 1)
        ) for _index, user_id in enumerate(user_ids)
    ]
    mock.return_value = user_dtos
    return mock


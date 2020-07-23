import datetime
import pytest
from freezegun import freeze_time


class TestGetPostPresenter:

    def test_raise_exception_for_invalid_post(self):
        from fb_post_clean_arch_v2.presenters.get_post_presenter import \
            GetPostPresenter
        from fb_post_clean_arch_v2.constants.exception_messages import \
            INVALID_POST_ID
        presenter = GetPostPresenter()
        expected_response = INVALID_POST_ID[0]
        response_status_code = INVALID_POST_ID[1]

        response_object = presenter.raise_exception_for_invalid_post()
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    @freeze_time("2020-01-1 05:21:34")
    def test_get_post_details_given_post_dto_returns_post_details(
            self, mocker, get_post_response):
        from fb_post_clean_arch_v2.presenters.get_post_presenter import \
            GetPostPresenter
        from fb_post_clean_arch_v2.tests.factories.storage_dtos import \
            PostDtoFactory, CommentDtoFactory, ReactionDtoFactory
        from fb_post_clean_arch_v2.tests.common_fixtures.adapters.\
            auth_service import prepare_get_user_dtos_mock
        from fb_post_clean_arch_v2.interactors.presenter_interfaces.\
            dtos import PostCompleteDetailsDto

        time = datetime.datetime.now()
        user_ids = [1, 2]
        post_dto = PostDtoFactory(pub_date_time=time)
        get_user_dtos_mock_method = prepare_get_user_dtos_mock(mocker, user_ids)
        user_dtos = get_user_dtos_mock_method(user_ids)
        comment_dto_1 = CommentDtoFactory(post_id=1,
                                          pub_date_time=time,
                                          parent_comment=None)
        reply_dto_1 = CommentDtoFactory(pub_date_time=time, parent_comment=1,
                                        user_id=1)
        comment_dtos = [comment_dto_1, reply_dto_1]
        reaction_dtos = ReactionDtoFactory.create_batch(2, post_id=1,
                                                        comment_id=None)
        post_complete_details_dto = PostCompleteDetailsDto(
            post_dto=post_dto,
            user_dtos=user_dtos,
            reactions_dto=reaction_dtos,
            comments_dto=comment_dtos
        )

        presenter = GetPostPresenter()
        response_object = presenter.get_response_for_get_post_details(
            post_complete_details_dto)

        import json
        response = json.loads(response_object.content)

        assert get_post_response == response

    @pytest.fixture()
    def get_post_response(self):
        get_post_response = {
            'post_content': 'post_content_1',
            'post_id': 1,
            'posted_at': '01-01-2020,05:21:1577836294.000000',
            'posted_by': {
                'profile_pic': 'profile_1',
                'user_id': 1,
                'name': 'user_1'
            },
            'reactions': {
                'count': 2,
                'type': [
                    'LIKE',
                    'WOW'

                ]
            },
            'comments': [
                {
                    'comment_id': 1,
                    'commenter': {
                        'user_id': 1,
                        'name': 'user_1',
                        'profile_pic': 'profile_1'
                    },
                    'commented_at': '01-01-2020,05:21:1577836294.000000',
                    'comment_content': 'comment_content_1',
                    'reactions': {
                        'count': 0,
                        'type': [

                        ]
                    },
                    'replies_count': 1,
                    'replies': [
                        {
                            'comment_id': 2,
                            'commenter': {
                                'user_id': 1,
                                'name': 'user_1',
                                'profile_pic': 'profile_1'
                            },
                            'commented_at': '01-01-2020,05:21:1577836294.000000',
                            'comment_content': 'comment_content_2',
                            'reactions': {
                                'count': 0,
                                'type': [

                                ]
                            }
                        }
                    ]
                }
            ],
            "comments_count": 1
        }
        return get_post_response

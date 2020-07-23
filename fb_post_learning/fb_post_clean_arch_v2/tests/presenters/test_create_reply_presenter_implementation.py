class TestCreateReplyPresenterImplementation:

    def test_raise_exception_for_invalid_comment_id(self):
        from fb_post_clean_arch_v2.presenters.create_reply_presenter_implementation import \
            CreateReplyPresenterImplementation
        presenter = CreateReplyPresenterImplementation()
        from fb_post_clean_arch_v2.constants.exception_messages import \
            INVALID_COMMENT_ID
        expected_response = INVALID_COMMENT_ID[0]
        response_status_code = INVALID_COMMENT_ID[1]

        response_object = presenter.raise_exception_for_invalid_comment_id()
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_get_response_given_comment_id_return_comment_id_dict(self):
        from fb_post_clean_arch_v2.presenters.create_reply_presenter_implementation import \
            CreateReplyPresenterImplementation
        presenter = CreateReplyPresenterImplementation()
        comment_id = 1
        expected_response = {
            "comment_id": comment_id
        }
        response_object = presenter.get_response(reply_id=comment_id)

        import json
        actual_response = json.loads(response_object.content)

        assert actual_response == expected_response

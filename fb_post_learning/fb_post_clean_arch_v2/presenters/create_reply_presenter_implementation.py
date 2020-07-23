from django.http import response
from fb_post_clean_arch_v2.interactors.presenter_interfaces.presenter_interface import \
    CreateReplyPresenterInterface


class CreateReplyPresenterImplementation(CreateReplyPresenterInterface):

    def raise_exception_for_invalid_comment_id(self) -> response.HttpResponse:
        from fb_post_clean_arch_v2.constants.exception_messages import \
            INVALID_COMMENT_ID
        import json
        data = json.dumps({
                "response": INVALID_COMMENT_ID[0],
                "http_status_code": 400,
                "res_status": INVALID_COMMENT_ID[1]
            })
        response_object = response.HttpResponse(data, 400)
        return response_object

    def get_response(self, reply_id: int) -> response.HttpResponse:
        import json
        data = json.dumps({"comment_id": reply_id})
        response_object = response.HttpResponse(
            data, status=201
        )
        return response_object

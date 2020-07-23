from fb_post_clean_arch_v2.utils.datetime_utils import get_datetime_as_string


class PresenterMixin:
    @staticmethod
    def get_user_details(user_dto):
        user_details_dict = {
            "user_id": user_dto.user_id,
            "name": user_dto.name,
            "profile_pic": user_dto.profile_pic_url
        }
        return user_details_dict

    def convert_comment_to_dict(self, reply, user_dto_dict):
        comment_details = {
            "comment_id": reply.comment_id,
            "commenter": self.get_user_details(user_dto_dict[reply.user_id]),
            "commented_at": get_datetime_as_string(reply.pub_date_time),
            "comment_content": reply.comment_content
        }
        return comment_details

    @staticmethod
    def get_reaction_dict(reaction_count, reactions_list):
        reaction_dict = {
            "count": reaction_count,
            "type": reactions_list
        }
        return reaction_dict

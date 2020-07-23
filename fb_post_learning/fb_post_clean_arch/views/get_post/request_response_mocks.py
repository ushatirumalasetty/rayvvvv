


RESPONSE_200_JSON = """
{
    "post_id": 1,
    "posted_by": {
        "user_id": 1,
        "name": "string",
        "profile_pic_url": "string"
    },
    "posted_at": "2099-12-31 00:00:00",
    "post_content": 1,
    "reactions": {
        "reaction_type": "HAHA"
    },
    "comments": [
        {
            "comment_id": 1,
            "commenter": {
                "user_id": 1,
                "name": "string",
                "profile_pic_url": "string"
            },
            "commented_at": "2099-12-31 00:00:00",
            "comment_content": "string",
            "reactions": {
                "reaction_type": "HAHA"
            },
            "replies_count": 1,
            "replies": [
                {
                    "comment_id": 1,
                    "commenter": {
                        "user_id": 1,
                        "name": "string",
                        "profile_pic_url": "string"
                    },
                    "commented_at": "2099-12-31 00:00:00",
                    "comment_content": "string",
                    "reactions": {
                        "reaction_type": "HAHA"
                    }
                }
            ]
        }
    ],
    "comment_count": 1
}
"""


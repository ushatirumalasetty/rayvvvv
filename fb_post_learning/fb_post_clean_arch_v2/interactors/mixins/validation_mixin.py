class ValidationMixin:
    def validate_post_id(self, post_id: int):
        self.storage.validate_post_id(post_id=post_id)



class ServiceAdapter:
    @property
    def auth_service(self):
        from fb_post_clean_arch_v2.adapters.auth_service import AuthService
        return AuthService()


def get_service_adapter():
    return ServiceAdapter()

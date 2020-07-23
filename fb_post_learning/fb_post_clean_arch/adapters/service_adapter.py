class ServiceAdapter:

    @property
    def auth_service(self):
        from .auth_service import AuthService
        return AuthService()


    @property
    def reactions_service(self):
        from .reactions_service import ReactionsService
        return ReactionsService()

def get_service_adapter():
    return ServiceAdapter()



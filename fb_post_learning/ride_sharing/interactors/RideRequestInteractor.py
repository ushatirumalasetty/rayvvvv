from datetime import datetime

from ride_sharing.constants.constants import EMAIL_CONTENT_FOR_NEW_RIDE_REQUEST_NOTIFICATION_FOR_ADMIN, \
    EMAIL_SUBJECT_FOR_NEW_RIDE_REQUEST_NOTIFICATION_FOR_ADMIN
from ride_sharing.exceptions.custom_exceptions import InvalidFromPlaceException, InvalidToPlaceException, \
    InvalidTravelDateTimeException, InvalidNumberOfSeatsException
from ride_sharing.interactors.storages.dtos.dtos import RideRequestDTO
from ride_sharing.interactors.storages.storage_interface import StorageInterface


class RideRequestInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_ride_request(self, ride_request: RideRequestDTO):
        self._validate_from_place(ride_request.from_place)
        self._validate_to_place(ride_request.to_place)
        self._validate_travel_datetime(ride_request.travel_datetime)
        self._validate_number_of_seats(ride_request.number_of_seats_required)
        self.storage.create_ride_request(ride_request=ride_request)
        self._notify_admin()

    @staticmethod
    def _validate_from_place(from_place: str):
        if not from_place:
            raise InvalidFromPlaceException()

    @staticmethod
    def _validate_to_place(to_place: str):
        if not to_place:
            raise InvalidToPlaceException()

    @staticmethod
    def _validate_travel_datetime(travel_datetime: datetime):
        current_datetime = datetime.now()
        if current_datetime >= travel_datetime:
            raise InvalidTravelDateTimeException()

    @staticmethod
    def _validate_number_of_seats(number_of_seats):
        if not isinstance(number_of_seats, int) or number_of_seats <= 0:
            raise InvalidNumberOfSeatsException()

    @staticmethod
    def _notify_admin():
        from ride_sharing.interactors.user_details_interactor import UserDetailsInteractor
        from ride_sharing.interactors.email_notification_interactor import EmailNotificationInteractor
        user_details_interactor = UserDetailsInteractor()
        admin_email = user_details_interactor.get_admin_email()

        email_notification_interactor = EmailNotificationInteractor()
        email_notification_interactor.send_email(
            mail_id=admin_email,
            content=EMAIL_CONTENT_FOR_NEW_RIDE_REQUEST_NOTIFICATION_FOR_ADMIN,
            subject=EMAIL_SUBJECT_FOR_NEW_RIDE_REQUEST_NOTIFICATION_FOR_ADMIN
        )

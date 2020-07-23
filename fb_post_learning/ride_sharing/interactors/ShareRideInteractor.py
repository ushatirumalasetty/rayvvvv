from datetime import datetime
from ride_sharing.constants.constants import EMAIL_CONTENT_FOR_NEW_RIDE_REQUEST_NOTIFICATION_FOR_ADMIN, \
    EMAIL_SUBJECT_FOR_NEW_RIDE_REQUEST_NOTIFICATION_FOR_ADMIN
from ride_sharing.exceptions.custom_exceptions import InvalidFromPlaceException, InvalidToPlaceException, \
    InvalidStartDateTimeException, InvalidNumberOfSeatsException, InvalidCarNo
from ride_sharing.interactors.storages.dtos.dtos import ShareRideDTO
from ride_sharing.interactors.storages.storage_interface import StorageInterface


class ShareRideInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def share_ride(self, share_ride: ShareRideDTO):
        self._validate_from_place(share_ride.from_place)
        self._validate_to_place(share_ride.to_place)
        self._validate_start_datetime(share_ride.start_datetime)
        self._validate_car_no(share_ride.car_no)
        self._validate_number_of_seats(share_ride.number_of_seats_required)
        self.storage.share_ride(share_ride=share_ride)
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
    def _validate_start_datetime(start_datetime: datetime):
        current_datetime = datetime.now()
        if current_datetime >= start_datetime:
            raise InvalidStartDateTimeException()

    @staticmethod
    def _validate_number_of_seats(number_of_seats):
        if not isinstance(number_of_seats, int) or number_of_seats <= 0:
            raise InvalidNumberOfSeatsException()
    
    @staticmethod
    def _validate_car_no(car_no):
        if not isinstance(car_no, int) or car_no <= 0:
            raise InvalidCarNo()

    
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


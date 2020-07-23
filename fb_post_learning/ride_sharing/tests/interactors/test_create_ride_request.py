from datetime import datetime
import pytest
from mock import create_autospec, patch
from freezegun import freeze_time

from ride_sharing.constants.constants import EMAIL_SUBJECT_FOR_NEW_RIDE_REQUEST_NOTIFICATION_FOR_ADMIN, \
    EMAIL_CONTENT_FOR_NEW_RIDE_REQUEST_NOTIFICATION_FOR_ADMIN
from ride_sharing.exceptions.custom_exceptions import InvalidFromPlaceException, InvalidToPlaceException, \
    InvalidTravelDateTimeException, InvalidNumberOfSeatsException
from ride_sharing.interactors.RideRequestInteractor import RideRequestInteractor
from ride_sharing.interactors.storages.dtos.dtos import RideRequestDTO
from ride_sharing.interactors.storages.storage_interface import StorageInterface


class TestCreateRideRequest:

    @freeze_time("2020-10-10 12:00:00")
    def test_create_ride_request(self):
        # Setup
        storage = create_autospec(StorageInterface)
        interactor = RideRequestInteractor(storage=storage)
        ride_request_dto = RideRequestDTO(
            from_place="Kurnool",
            to_place="Hyderabad",
            travel_datetime=datetime(year=2020, month=10, day=19, hour=12),
            number_of_seats_required=2
        )

        # Act
        interactor.create_ride_request(ride_request=ride_request_dto)

        # Assert
        storage.create_ride_request.assert_called_once_with(
            ride_request=ride_request_dto)

    def test_create_ride_request_when_from_place_given_as_empty_raise_exception(self):
        # Setup
        storage = create_autospec(StorageInterface)                                             
        interactor = RideRequestInteractor(storage=storage)
        ride_request_dto = RideRequestDTO(
            from_place="",
            to_place="Hyderabad",
            travel_datetime=datetime(year=2020, month=10, day=19, hour=12),
            number_of_seats_required=2
        )

        # Act

        with pytest.raises(InvalidFromPlaceException) as err:
            interactor.create_ride_request(ride_request=ride_request_dto)

        # Assert
        storage.create_ride_request.assert_not_called()

    def test_create_ride_request_when_to_place_given_as_empty_raise_exception(self):
        # Setup
        storage = create_autospec(StorageInterface)
        interactor = RideRequestInteractor(storage=storage)
        ride_request_dto = RideRequestDTO(
            from_place="Kurnool",
            to_place="",
            travel_datetime=datetime(year=2020, month=10, day=19, hour=12),
            number_of_seats_required=2
        )

        # Act

        with pytest.raises(InvalidToPlaceException) as err:
            interactor.create_ride_request(ride_request=ride_request_dto)

        # Assert
        storage.create_ride_request.assert_not_called()

    @freeze_time("2020-10-20 12:00:00")
    def test_create_ride_request_when_travel_datetime_less_than_current_datetime_raise_exception(self):
        # Setup
        storage = create_autospec(StorageInterface)
        interactor = RideRequestInteractor(storage=storage)
        ride_request_dto = RideRequestDTO(
            from_place="Kurnool",
            to_place="Hyderabad",
            travel_datetime=datetime(year=2020, month=10, day=19, hour=12),
            number_of_seats_required=2
        )

        with pytest.raises(InvalidTravelDateTimeException) as err:
            interactor.create_ride_request(ride_request=ride_request_dto)

        # Assert
        storage.create_ride_request.assert_not_called()

    @freeze_time("2020-10-10 12:00:00")
    def test_create_ride_request_when_number_of_seats_required_is_not_positive_integer_raise_exception(self):
        # Setup
        storage = create_autospec(StorageInterface)
        interactor = RideRequestInteractor(storage=storage)
        ride_request_dto = RideRequestDTO(
            from_place="Kurnool",
            to_place="Hyderabad",
            travel_datetime=datetime(year=2020, month=10, day=19, hour=12),
            number_of_seats_required=-1
        )

        # Act
        with pytest.raises(InvalidNumberOfSeatsException) as err:
            interactor.create_ride_request(ride_request=ride_request_dto)

        # Assert
        storage.create_ride_request.assert_not_called()

    @freeze_time("2020-10-10 12:00:00")
    @patch('ride_sharing.interactors.email_notification_interactor.EmailNotificationInteractor.send_email')
    @patch('ride_sharing.interactors.user_details_interactor.UserDetailsInteractor.get_admin_email')
    def test_when_ride_request_is_created_then_send_notification_to_admin(
            self, get_admin_email_mock, send_email_mock):
        # Setup
        storage = create_autospec(StorageInterface)
        interactor = RideRequestInteractor(storage=storage)
        ride_request_dto = RideRequestDTO(
            from_place="Kurnool",
            to_place="Hyderabad",
            travel_datetime=datetime(year=2020, month=10, day=19, hour=12),
            number_of_seats_required=2
        )
        admin_email = 'test@example.com'
        email_content = EMAIL_CONTENT_FOR_NEW_RIDE_REQUEST_NOTIFICATION_FOR_ADMIN
        email_subject = EMAIL_SUBJECT_FOR_NEW_RIDE_REQUEST_NOTIFICATION_FOR_ADMIN
        get_admin_email_mock.return_value = admin_email

        # Act
        interactor.create_ride_request(ride_request=ride_request_dto)

        # Assert
        get_admin_email_mock.assert_called_once()
        send_email_mock.assert_called_once_with(
            mail_id=admin_email, content=email_content, subject=email_subject)

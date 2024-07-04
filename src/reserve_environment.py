from digitalai.release.integration import BaseTask
from digitalai.release.v1.api.application_api import ApplicationApi
from digitalai.release.v1.api.application_api import ApplicationFilters
from digitalai.release.v1.api.environment_api import EnvironmentApi
from digitalai.release.v1.api.environment_api import EnvironmentFilters
from digitalai.release.v1.api.environment_reservation_api import EnvironmentReservationApi
from digitalai.release.v1.api.environment_reservation_api import EnvironmentReservationForm
import datetime


class ReserveEnvironment(BaseTask):
    """
        Sets the system message in the Release UI by invoking the API.
    """

    def execute(self) -> None:

        # Create the REST clients
        application_api = ApplicationApi(self.get_default_api_client())
        environment_api = EnvironmentApi(self.get_default_api_client())
        reservation_api = EnvironmentReservationApi(self.get_default_api_client())

        # Get App & Env
        apps = application_api.search_applications(application_filters = ApplicationFilters(title="App"))
        envs = environment_api.search_environments(environment_filters = EnvironmentFilters(title="Env"))

        # Create the reservation
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)

        reservation = EnvironmentReservationForm(
            start_date=datetime.datetime.now(),
            end_date=tomorrow,
            note="Created from ReserveEnvironment task",
            environment_id=envs[0].id,
            application_ids=[apps[0].id]
        )
        reservation_api.create_reservation(environment_reservation_form=reservation)

        # Add a line to the comment section in the UI
        self.add_comment(f"Added reservation")

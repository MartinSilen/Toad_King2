import threading

from main.common.external.dao.dao_location import DaoLocationImplementation
from main.common.abstracts.services.location_service import AbstractLocationService
from main.common.external.models.location import Location


class LocationServiceImplementation(AbstractLocationService):
    _DAO_LOCATION = DaoLocationImplementation()
    lock = threading.Lock()

    def create_new_location(self, location_id, kwargs):
        location = Location(external_id=location_id, **kwargs)
        with self.lock:
            self._DAO_LOCATION.insert(location)

    def get_location(self, location_id):
        with self.lock:
            return self._DAO_LOCATION.find_by_id(location_id)

    def update_location(self, location: Location):
        with self.lock:
            self._DAO_LOCATION.update(location)

    def delete_location(self, location_id):
        with self.lock:
            self._DAO_LOCATION.delete_by_id(location_id)







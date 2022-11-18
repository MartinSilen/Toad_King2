from abc import ABC
from main.common.external.models.location import Location


class AbstractLocationService(ABC):

    def create_new_location(self, location_id, kwargs):
        ...

    def get_location(self, location_id):
        ...

    def update_location(self, location: Location):
        ...

    def delete_location(self, location_id):
        ...

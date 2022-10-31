import threading
from abc import ABC, abstractmethod

from gamedatabase import DatabaseInterface

LOCATION_FIELDS = ['visitor_ids', 'event_ids']


class LocationManagerInterface(ABC):

    @abstractmethod
    def get_location_info(self, location_name: str, field_name=None):
        pass

    @abstractmethod
    def modify_location_info(self, location_name, value, new_value):
        pass


class LocationManager(LocationManagerInterface):

    def __init__(self, locations_database: DatabaseInterface):
        self.locations_database = locations_database
        self.lock = threading.Lock()

    def get_location_info(self, location_name: str, field=None):
        if field is not None:
            return self.locations_database.get_value(location_name, field)
        else:
            return self.locations_database.get_line_as_dict(location_name)

    def modify_location_info(self, location_name, value, new_value):
        if isinstance(self.locations_database.get_value(location_name, value), new_value.__class__):
            self.locations_database.modify_value(location_name, value, new_value)
        else:
            raise TypeError

from abc import ABC, abstractmethod
from locations import LocationManagerInterface
from users import UserManagerInterface
from gamedatabase import DatabaseInterface

class EventInterface(ABC):

    @abstractmethod
    def event_update(self):
        pass

class Event(EventInterface):
    def __init__(self, event_location, user_manager, location_manager, event_manager, object_manager):
        self.user_manager = user_manager
        self.location_manager = location_manager
        self.event_manager = event_manager
        self.object_manager = object_manager
        self.event_location = event_location

    @abstractmethod
    def event_update(self):
        pass

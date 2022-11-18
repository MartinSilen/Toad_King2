from main.common.external.models.location import Location


class ActiveLocationDict:

    def __init__(self):
        self.storage = {}

    def add_active_location(self, location: Location):
        self.storage[location.external_id] = location

    def get_active_location(self, location_id):
        return self.storage[location_id]

    def update_active_location(self, location_id, location: Location):
        self.storage[location_id] = location

    def delete_active_location(self, location_id):
        self.storage.pop(location_id)
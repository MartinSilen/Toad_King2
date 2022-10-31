import commandhandlers
user_manager = 1
location_manager = 2
event_manager = 3

def test_create_handler():
    handler_factory = commandhandlers.CommandHandlerFactory(user_manager, location_manager, event_manager)
    new_user_handler = handler_factory.create_handler('greenvale_handler', 111)
    assert new_user_handler.user_id == 111
    assert new_user_handler.user_manager == 1
    assert new_user_handler.location_manager == 2
    assert new_user_handler.event_manager == 3

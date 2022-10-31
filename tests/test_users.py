import pytest

import gamedatabase
import users

test_users_dict = {'user_id': [12345, 23456, 56789], 'username': ['Jojo', 'Kiki', 'Rori'],
                     'user_location': ['greenvale', 'river_bank', 'forest']}

def test_add_new_user():
    assert False


def test_create_active_user():
    user_database = gamedatabase.PandasDatabase()
    user_database.initialize_from_dict(test_users_dict, 'user_id')
    user_manager = users.UserManager(user_database)
    user_manager.create_active_user(12345)
    assert 12345 in user_manager.active_users
    assert user_manager.active_users[12345].user_info == {'username': 'Jojo', 'user_location': 'greenvale'}


def test_is_in_active_users():
    assert False


def test_ensure_user_initialization():
    assert False


def test_get_user_info():
    assert False


def test_modify_user_info():
    user_database = gamedatabase.PandasDatabase()
    user_database.initialize_from_dict(test_users_dict, 'user_id')
    user_manager = users.UserManager(user_database)
    user_manager.modify_user_info(12345, 'username', 'Nathan')
    assert user_manager.get_user_info(12345, 'username') == 'Nathan'

def test_modify_user_info_type_mismatch():
    user_database = gamedatabase.PandasDatabase()
    user_database.initialize_from_dict(test_users_dict, 'user_id')
    user_manager = users.UserManager(user_database)
    with pytest.raises(TypeError):
        user_manager.modify_user_info(12345, 'username', 3.4)

def test_save_active_user():
    user_database = gamedatabase.PandasDatabase()
    user_database.initialize_from_dict(test_users_dict, 'user_id')
    user_manager = users.UserManager(user_database)
    user_manager.modify_user_info(12345, 'username', 'Nathan')
    assert user_database.get_value(12345, 'username') != 'Nathan'
    user_manager.save_active_user(12345)
    assert user_database.get_value(12345, 'username') == 'Nathan'

def test_deactivate_user():
    user_database = gamedatabase.PandasDatabase()
    user_database.initialize_from_dict(test_users_dict, 'user_id')
    user_manager = users.UserManager(user_database)
    assert user_manager.is_in_active_users(12345) is False
    print(user_manager.get_user_info(12345, 'user_location'))
    assert user_manager.is_in_active_users(23456) is False
    assert user_manager.is_in_active_users(12345) is True
    user_manager.deactivate_user(12345)
    assert user_manager.is_in_active_users(12345) is False

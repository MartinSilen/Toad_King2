import logging

from bson import ObjectId

from main.common.external.dao.dao_user import DaoUserImplementation
from main.common.external.models.active_ability import ActiveAbility
from main.common.external.models.user import User

def test_prepare_database():
    user_dao = DaoUserImplementation()
    user_dao._get_collection().create_index('external_id', unique=True)


def test_find_by_id():
    user_dao = DaoUserImplementation()
    active_ability1 = ActiveAbility('ability1', 2)
    active_ability2 = ActiveAbility('ability2', 0)
    user_dao.delete_by_id('234')
    user_dao.delete_by_id('123')
    new_user2 = User('123', character_name='test_user2', character_active_abilities=[active_ability1])
    new_user = User('234', character_name='test_user2', character_active_abilities=[active_ability1, active_ability2])
    user_dao.insert(new_user)
    user_dao.insert(new_user2)
    print(user_dao.find_by_id('123'))
    print(user_dao.find_by_id('234'))

def test_update_by_id():
    user_dao = DaoUserImplementation()
    active_ability1 = ActiveAbility('ability1', 2)
    active_ability2 = ActiveAbility('ability2', 0)
    user_dao.delete_by_id('234')
    user_dao.delete_by_id('123')
    new_user2 = User('123', character_name='test_user2', character_active_abilities=[active_ability1])
    new_user = User('234', character_name='test_user2', character_active_abilities=[active_ability1, active_ability2])
    user_dao.insert(new_user)
    user_dao.insert(new_user2)
    new_user2.character_name = 'updated_name2'
    new_user.character_name = 'updated_name'
    user_dao.update(new_user2)
    user_dao.update(new_user)
    print(user_dao.find_by_id('123'))
    print(user_dao.find_by_id('234'))


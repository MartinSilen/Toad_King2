from main.common.external.models.user import User


def test_user():
    user = User(external_id='1', character_name='test', character_class='knight', character_race='fae', character_description='double_test')
    print(str(user))

from main.common.business.services.redis_service import RedisServiceImplementation
from main.common.external.models.user import User


def test_add_active_user():
    redis_service = RedisServiceImplementation()
    redis_service.add_active_user(User('123', 'Doe'))
    resulting_user = redis_service.get_active_user('123')
    print(resulting_user)


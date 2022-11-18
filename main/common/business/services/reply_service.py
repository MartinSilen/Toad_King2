import threading


from main.common.external.dao.dao_reply import DaoReplyImplementation
from main.common.external.models.user import User


class ReplyServiceImplementation:
    _DAO_REPLY = DaoReplyImplementation()
    lock = threading.Lock()


    def get_reply(self, reply_id):
        return self._DAO_REPLY.find_by_id(reply_id)



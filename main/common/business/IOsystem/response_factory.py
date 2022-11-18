from main.common.business.models.response_class import Response
from main.common.external.dao.dao_reply import DaoReplyImplementation

reply_dao = DaoReplyImplementation()

def construct_response(user_id, response_id=None, additional_text: str= ''):
    if response_id is None:
        response_text = ''
    else:
        response_text = reply_dao.find_by_id(response_id)
    response_text = response_text + additional_text
    return Response(user_id=user_id, message=response_text)
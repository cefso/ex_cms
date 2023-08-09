from pydantic import BaseModel


class OutGoingSchema(BaseModel):
    at_users: list
    chatbot_corp_id: str = None
    chatbot_user_id: str
    conversation_id: str
    conversation_title: str = None
    conversation_type: str
    create_at: int
    is_admin: bool = None
    is_in_at_list: bool = None
    msg_id: str
    msgtype: str
    sender_corp_id: str
    sender_id: str = None
    sender_nick: str
    sender_staff_id: str = None
    session_webhook: str
    session_webhook_expired_time: int
    text: str


class SignHeaderSchema(BaseModel):
    timestamp: str
    sign: str

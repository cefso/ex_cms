from pydantic import BaseModel


class Content(BaseModel):
    content: str = None


class AtUsers(BaseModel):
    dingtalkId: str = None
    staffId: str = None


class OutGoingSchema(BaseModel):
    atUsers: list = None
    chatbotCorpId: str = None
    chatbotUserId: str
    conversationId: str
    conversationTitle: str = None
    conversationType: str
    createAt: int
    isAdmin: bool = None
    isInAtList: bool = None
    msgId: str
    msgtype: str
    senderCorpId: str = None
    senderId: str
    senderNick: str
    senderStaffId: str = None
    sessionWebhook: str
    sessionWebhookExpiredTime: int
    text: Content = None

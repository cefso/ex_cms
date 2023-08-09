from pydantic import BaseModel


class OutGoingSchema(BaseModel):
    atUsers: list
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
    senderCorpId: str
    senderId: str = None
    senderNick: str
    senderStaffId: str = None
    sessionWebhook: str
    sessionWebhookExpiredTime: int
    text: str


# class SignHeaderSchema(BaseModel):
#     timestamp: str
#     sign: str

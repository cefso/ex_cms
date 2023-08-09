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
    senderCorpId: str = None
    senderId: str
    senderNick: str
    senderStaffId: str = None
    sessionWebhook: str
    sessionWebhookExpiredTime: int
    text: dict

# class SignHeaderSchema(BaseModel):
#     timestamp: str
#     sign: str

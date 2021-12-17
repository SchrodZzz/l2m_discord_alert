import requests

from src.utils.custom_log import Logger
from localization.en_contsts import SEND_MESSAGE_BODY, SEND_MESSAGE_REQUEST_RESULT


class RequestSender:

    @staticmethod
    def send(url, json):
        Logger.log(SEND_MESSAGE_BODY.format(json=json))
        res = requests.post(url, json=json)
        body = res if res != '' else '<Empty>'
        Logger.log(SEND_MESSAGE_REQUEST_RESULT(code=res, body=body))
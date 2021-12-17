import schedule
import requests

import time
from datetime import date
from datetime import datetime

from decouple import config

from localization.en_contsts import *


# MARK: Consts

URL = config('WEB_HOOK_PROD')
CATACOMBS_IMAGE_URL = 'https://drive.google.com/uc?id=1DzlGprLidB-94gsODYm95Y8IMgG-oS9u'
ORK_IMAGE_URL = 'https://drive.google.com/uc?id=1H516rg3kYjyDlcsuPSN-x-xorALXx5O2'


# MARK: Utils

def log(str):
    print(f'[{date.today()}, {datetime.now().strftime("%H:%M:%S")}] {str}')


def send_msg(json):
    log(SEND_MESSAGE_BODY.format(json=json))
    res = requests.post(URL, json=json)
    body = res if res != '' else '<Empty>'
    log(SEND_MESSAGE_REQUEST_RESULT(code=res, body=body))


def form_json_for_discord_image(text: str, image_url: str):
    json = {
        'content': text,
        'embeds': [
            {
                'image': {'url': image_url},
                'height': 300,
                'width': 300
            }
        ]
    }
    return json


def form_json_for_discord_blocks(text: str, first_title: str, first_subtitle: str, second_title: str, second_subtitle):
    json = {
        'content': text,
        'embeds': [
            {'title': first_title, 'description': first_subtitle},
            {'title': second_title, 'description': second_subtitle}
        ]
    }
    return json


# MARK: Setters

def set_alert_every_hour(job):
    schedule.every().hour.do(job)


def set_alert_every_day(time: str, job):
    schedule.every().day.at(time).do(job)


def set_alert_every_weekday(time: str, job):
    schedule.every().monday.at(time).do(job)
    schedule.every().tuesday.at(time).do(job)
    schedule.every().wednesday.at(time).do(job)
    schedule.every().thursday.at(time).do(job)
    schedule.every().friday.at(time).do(job)


def set_notify_catacombs():

    def notify():
        json = form_json_for_discord_image(
            CATACOMBS_TITLE,
            CATACOMBS_IMAGE_URL
        )
        send_msg(json)
        log(CATACOMBS_LOG_MSG)

    set_alert_every_weekday('09:19', notify)
    set_alert_every_weekday('17:49', notify)
    log(CATACOMBS_LOG_IS_SET)


def set_notify_ork():

    def notify():
        json = form_json_for_discord_image(
            ORKS_TITLE,
            ORK_IMAGE_URL
        )
        send_msg(json)
        log(ORKS_LOG_MSG)

    set_alert_every_day('09:29', notify)
    set_alert_every_day('17:29', notify)
    log(ORKS_LOG_IS_SET)


def set_notify_rift_guys():

    def notify_day():
        json = form_json_for_discord_blocks(
            RIFT_BOSSES_TITLE,
            RIFT_BOSSES_DAY_FIRST_TITLE,
            RIFT_BOSSES_DAY_FIRST_SUBTITLE,
            RIFT_BOSSES_DAY_SECOND_TITLE,
            RIFT_BOSSES_DAY_SECOND_SUBTITLE
        )
        send_msg(json)
        log(RIFT_BOSESS_DAY_LOG_MSG)

    def notify_night():
        json = form_json_for_discord_blocks(
            RIFT_BOSSES_TITLE,
            RIFT_BOSSES_NIGHT_FIRST_TITLE,
            RIFT_BOSSES_NIGHT_FIRST_SUBTITLE,
            RIFT_BOSSES_NIGHT_SECOND_TITLE,
            RIFT_BOSSES_NIGHT_SECOND_SUBTITLE
        )
        send_msg(json)
        log(RIFT_BOSESS_NIGHT_LOG_MSG)

    set_alert_every_day('08:59', notify_day)
    set_alert_every_day('16:59', notify_night)
    log(RIFT_BOSSES_LOG_IS_SET)


def set_ping_log():

    def ping_log():
        log(PING_LOG_MSG)

    set_alert_every_hour(ping_log)
    log(PING_LOG_IS_SET)


# MARK: Lifecycle

def main():
    set_ping_log()
    return

    set_notify_catacombs()
    set_notify_ork()
    set_notify_rift_guys()

    while True:
        schedule.run_pending()
        time.sleep(5)


main()
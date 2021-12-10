import schedule
import requests

import time
from datetime import date
from datetime import datetime

from decouple import config


# MARK: Consts

URL = config('WEB_HOOK_PROD')
CATACOMBS_IMAGE_URL = 'https://drive.google.com/uc?id=1DzlGprLidB-94gsODYm95Y8IMgG-oS9u'
WOLF_IMAGE_URL = 'https://drive.google.com/uc?id=1eeGM0zPv0WDScde4eDDJX7UFBavX5BgT'


# MARK: Utils

def log(func):
    print(f'[{date.today()}, {datetime.now().strftime("%H:%M:%S")}] {func.__name__}')


def send_msg(json):
    requests.post(URL, json=json)


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
        json = form_json_for_discord_image('@here Регистрация в каты начнется через одну минуту', CATACOMBS_IMAGE_URL)
        send_msg(json)
        log(set_notify_catacombs)

    set_alert_every_weekday('09:29', notify)
    set_alert_every_weekday('17:49', notify)


def set_notify_wolf():

    def notify():
        json = form_json_for_discord_image('@here Волки заспавняться через одну минуту:wolf:', WOLF_IMAGE_URL)
        send_msg(json)
        log(set_notify_wolf)

    set_alert_every_day('09:29', notify)
    set_alert_every_day('17:29', notify)


def set_notify_rift_guys():

    def notify_day():
        json = form_json_for_discord_blocks(
            '@here Рейдовые боссы заспавнятся через одну минуту',
            ':boar: Васк',
            'Будет в локации \'Кровавые топи\'',
            ':cockroach: Крума',
            'Будет в локации \'Гибельный лес\''
        )
        send_msg(json)
        log(set_notify_rift_guys)

    def notify_night():
        json = form_json_for_discord_blocks(
            '@here Рейдовые боссы заспавнятся через одну минуту',
            ':bat: Райла',
            'Будет в локации \'Земля Казненных\'',
            ':fork_and_knife: Кастур',
            'Будет в локации \'Пограничная область орков Тимак\''
        )
        send_msg(json)
        log(set_notify_rift_guys)

    set_alert_every_day('08:59', notify_day)
    set_alert_every_day('16:59', notify_night)


def set_ping_log():

    def ping_log():
        log(ping_log)

    set_alert_every_hour(ping_log)


# MARK: Lifecycle

def main():
    set_ping_log()

    set_notify_catacombs()
    set_notify_wolf()
    set_notify_rift_guys()

    while True:
        schedule.run_pending()
        time.sleep(5)


main()
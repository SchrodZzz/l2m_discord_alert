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

def log(str):
    print(f'[{date.today()}, {datetime.now().strftime("%H:%M:%S")}] {str}')


def send_msg(json):
    log(f'Going to send message with body: {json}')
    res = requests.post(URL, json=json)
    log(f'Request result: {res.text}')


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
            '@here Регистрация в каты начнется через одну минуту:skull:',
            CATACOMBS_IMAGE_URL
        )
        send_msg(json)
        log("Notify catacombs")

    set_alert_every_weekday('09:29', notify)
    set_alert_every_weekday('17:49', notify)


def set_notify_wolf():

    def notify():
        json = form_json_for_discord_image(
            '@here Волки заспавнятся через одну минуту:wolf:',
            WOLF_IMAGE_URL
        )
        send_msg(json)
        log("Notify wolf")

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
        log("Notify day rift")

    def notify_night():
        json = form_json_for_discord_blocks(
            '@here Рейдовые боссы заспавнятся через одну минуту',
            ':bat: Райла',
            'Будет в локации \'Земля Казненных\'',
            ':fork_and_knife: Кастур',
            'Будет в локации \'Пограничная область орков Тимак\''
        )
        send_msg(json)
        log("Notify night rift")

    set_alert_every_day('08:59', notify_day)
    set_alert_every_day('16:59', notify_night)


def set_ping_log():

    def ping_log():
        log("I'm still alive")

    set_alert_every_hour(ping_log)


# MARK: Lifecycle

def main():
    set_ping_log()
    log("> Ping msg is set")

    set_notify_catacombs()
    log("> Catacombs alert is set")
    set_notify_wolf()
    log("> Wolfs alert is set")
    set_notify_rift_guys()
    log("> Rift bois alert is set")

    while True:
        schedule.run_pending()
        time.sleep(5)


main()
from localization.en_contsts import *
from src.utils.env_resolver import *
from src.utils.custom_log import Logger
from src.utils.scheduler import Scheduler
from src.network.json_encoder import JSONEncoder
from src.network.request_sender import RequestSender

# time on heroku is set to UTC+0000


class NotificationsSetter:

    @staticmethod
    def set_catacombs_notification():

        def notify():
            json = JSONEncoder.build_discord_msg_image(CATACOMBS_TITLE, CATACOMBS_IMAGE_URL)
            RequestSender.send(WEBHOOK_URL, json)
            Logger.log(CATACOMBS_LOG_MSG)

        Scheduler.set_alert_every_weekday('09:19', notify)
        Scheduler.set_alert_every_weekday('17:49', notify)
        Logger.log(CATACOMBS_IS_SET_LOG_MSG)

    @staticmethod
    def set_orks_notification():

        def notify():
            json = JSONEncoder.build_discord_msg_image(ORKS_TITLE, ORKS_IMAGE_URL)
            RequestSender.send(WEBHOOK_URL, json)
            Logger.log(ORKS_LOG_MSG)

        Scheduler.set_alert_every_day('09:29', notify)
        Scheduler.set_alert_every_day('17:29', notify)
        Logger.log(ORKS_IS_SET_LOG_MSG)

    @staticmethod
    def set_rift_bosses_notification():

        def notify_day_rift_bosses():
            json = JSONEncoder.build_discord_msg_blocks(
                RIFT_BOSSES_TITLE,
                RIFT_BOSSES_DAY_FIRST_TITLE,
                RIFT_BOSSES_DAY_FIRST_SUBTITLE,
                RIFT_BOSSES_DAY_SECOND_TITLE,
                RIFT_BOSSES_DAY_SECOND_SUBTITLE
            )
            RequestSender.send(WEBHOOK_URL, json)
            Logger.log(RIFT_BOSESS_DAY_LOG_MSG)

        def notify_night_rift_bosses():
            json = JSONEncoder.build_discord_msg_blocks(
                RIFT_BOSSES_TITLE,
                RIFT_BOSSES_NIGHT_FIRST_TITLE,
                RIFT_BOSSES_NIGHT_FIRST_SUBTITLE,
                RIFT_BOSSES_NIGHT_SECOND_TITLE,
                RIFT_BOSSES_NIGHT_SECOND_SUBTITLE
            )
            RequestSender.send(WEBHOOK_URL, json)
            Logger.log(RIFT_BOSESS_NIGHT_LOG_MSG)

        Scheduler.set_alert_every_day('08:59', notify_day_rift_bosses)
        Scheduler.set_alert_every_day('16:59', notify_night_rift_bosses)
        Logger.log(RIFT_BOSSES_IS_SET_LOG_MSG)

    @staticmethod
    def set_clan_bosses_notification():

        def notify():
            json = JSONEncoder.build_discord_msg_image(CLAN_BOSSES_TITLE, CLAN_BOSSES_IMAGE_URL)
            RequestSender.send(WEBHOOK_URL, json)
            Logger.log(CLAN_BOSSES_LOG_MSG)

        Scheduler.set_alert_every_sunday('09:00', notify)
        Logger.log(CLAN_BOSSES_IS_SET_LOG_MSG)

    @staticmethod
    def set_ping():
        
        def ping():
            Logger.log(PING_LOG_MSG)

        Scheduler.set_alert_every_hour(ping)
        Logger.log(PING_IS_SET_LOG_MSG)

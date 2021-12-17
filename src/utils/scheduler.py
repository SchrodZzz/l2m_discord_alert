import schedule


class Scheduler:

    @staticmethod
    def set_alert_every_hour(job):
        schedule.every().hour.do(job)

    @staticmethod
    def set_alert_every_day(time: str, job):
        schedule.every().day.at(time).do(job)

    @staticmethod
    def set_alert_every_sunday(time: str, job):
        schedule.every().sunday.at(time).do(job)

    @staticmethod
    def set_alert_every_weekday(time: str, job):
        schedule.every().monday.at(time).do(job)
        schedule.every().tuesday.at(time).do(job)
        schedule.every().wednesday.at(time).do(job)
        schedule.every().thursday.at(time).do(job)
        schedule.every().friday.at(time).do(job)
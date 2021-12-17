import src.network.router

from src.utils.run_loop import *
from src.utils.notifications_setter import NotificationsSetter


NotificationsSetter.set_ping()
NotificationsSetter.set_orks_notification()
NotificationsSetter.set_catacombs_notification()
NotificationsSetter.set_rift_bosses_notification()

start_run_loop(5)

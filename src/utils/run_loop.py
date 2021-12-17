import time
import schedule


def start_run_loop(tick: int):
    while True:
        schedule.run_pending()
        time.sleep(tick)
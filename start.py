from apscheduler.schedulers.blocking import BlockingScheduler

from task import Task


def job():
    t = Task()
    t.process()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', day_of_week='0-6', hour=18, minute=1, timezone='Asia/Shanghai')
    scheduler.start()

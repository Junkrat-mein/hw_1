#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    uses: yanzay / notify - telegram @ v0
    .1
    .0
    if: always()
    with:
        chat: ${{secrets.chat}}  # user id or channel name secret
        token: ${{secrets.token}}  # token secret
        status: ${{job.status}}  # do not modify this line


if __name__ == '__main__':
    run_tasks()

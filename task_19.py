#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while not wall_is_on_the_right():
        move_right()
    while not wall_is_above():
        move_up()

    while not wall_is_on_the_left():
        move_left()
    while not wall_is_above():
        move_up()



    move_right(5)
    if wall_is_on_the_right():
        bre
pass



if __name__ == '__main__':
    run_tasks()

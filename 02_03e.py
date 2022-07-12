from collections import deque
from threading import Thread


class Task(object):
    def __init__(self, taskDesc, hasPriority=False):
        self.hasPriority = hasPriority
        self.taskDesc = taskDesc
    def __str__(self):
        return "Task: {0}, Priority: {1} ".format(self.taskDesc,self.hasPriority)


task_queue = deque()

def add_task (task):
    if task.hasPriority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)

def do_task():
    return task_queue.popleft()

def print_tasks():
    for t in task_queue:
        print (t.taskDesc)

def main():
    print(task_queue)
    add_task(Task("Write List"))
    #print_tasks()
    add_task(Task("Make Breakfast"))
    add_task(Task("Respond to Email", True))
    print(task_queue)
    print_tasks()
    print(do_task())
    return

if __name__ == "__main__":
    main()
from Objects.Task import Task

tasks : list = []

tasks.append(Task('Задача 1'))
tasks.append(Task('Задача 2'))
tasks.append(Task('Задача 3'))

print(list(map(str,tasks)))
from task import *

class TaskManager:
    
    
    def __init__(self):
        self.tasks = set()
        self.subtasks = set()
        self.complex_tasks = set()
    
    def create_task(self, task):
        self.tasks.add(task)
    
    def create_subtask(self, subtask):
        for task in self.complex_tasks:
            if task.id == subtask.parent_id:
                task.subtasks.add(subtask)
                break
        else:
            raise Exception('complex task with given parent_id does not exist')
    
    def create_complex_task(self, complex_task):
        self.complex_tasks.add(complex_task)
    
    def get_tasks(self):
        return self.tasks
    
    def get_subtasks(self):
        return self.subtasks
    
    def get_complex_tasks(self):
        return self.complex_tasks
    
    def get_tasks_by_id(self, id):
        return {task for task in self.tasks if task.id == id}
    
    def get_subtasks_by_id(self, id):
        return {task for task in self.subtasks if task.id == id}
    
    def get_complex_tasks_by_id(self, id):
        return {task for task in self.complex_tasks if task.id == id}
    
    def remove_tasks(self, *tasks):
        self.tasks.difference(set(tasks))
    
    def remove_subtasks(self, *tasks):
        self.subtasks.difference(set(tasks))
    
    def remove_complex_tasks(self, *tasks):
        tasks_id = {task.id for task in tasks}
        subtasks = {task for task in self.subtasks if task.parent_id in tasks_id}
        self.subtasks.difference(subtasks)
        self.complex_tasks.difference(set(tasks))
    
    def remove_task_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                break
        else:
            raise Exception('there is no such id')
    
    def remove_subtask_by_id(self, id):
        for task in self.subtasks:
            if task.id == id:
                self.subtasks.remove(task)
                break
        else:
            raise Exception('there is no such id')
    
    def remove_complex_task_by_id(self, id):
        subtasks = {task for task in self.complex_tasks if task.parent_id == id}
        self.subtasks.difference(subtasks)
        for task in self.complex_tasks:
            if task.id == id:
                self.complex_tasks.remove(task)
                break
        else:
            raise Exception('there is no such id')

    def update_status(self, task, new_status):
        if task in self.tasks or task in self.subtasks or task in self.complex_tasks:
            task.status = new_status
        else:
            raise Exception('there is no such task')

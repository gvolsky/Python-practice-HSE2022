from task import *

class TaskManager:
    
    
    def __init__(self):
        self.tasks = []
        self.subtasks = []
        self.complex_tasks = []
    
    def create_task(self, id, name, description, status):
        self.tasks.append(
            Task(id, name, description, status)
        )
    
    def create_subtask(self, id, name, description, status, parent_id):
        subtask = Subtask(id, name, description, status, parent_id)
        for task in self.complex_tasks:
            if task.id == parent_id:
                task.subtasks.append(subtask)
                break
        else:
            raise Exception('complex task with given parent_id does not exist')
    
    def create_complex_task(self, id, name, description, status, *subtasks):
        self.complex_tasks.append(
            ComplexTask(id, name, description, status, *subtasks)
        )

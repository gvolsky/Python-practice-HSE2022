class Task:
    def __init__(self, id, name, description, status):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        

class Subtask(Task):
    # have comlex task id
    def __init__(self, id, name, description, status, parent_id):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id
    

class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self, id, name, description, status, subtask):
        super().__init__(id, name, description, status)
        self.subtasks = subtask   
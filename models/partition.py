class Partition:
    def __init__(self, pid, space_assigned, task):
        self.pid = pid
        self.space_assigned = space_assigned
        self.task = task

    def __str__(self):
        if self.task == None:
            return f'Particion de {self.space_assigned}Kb libre'
        else:
            return f'Particion de {self.space_assigned}Kb Ocupada con {self.task}'
 

    def __eq__(self, other):
        if isinstance(other, Partition):
            return self.pid == other.pid
        return False

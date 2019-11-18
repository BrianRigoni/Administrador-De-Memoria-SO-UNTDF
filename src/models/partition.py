class Partition:
    def __init__(self, pid, space_assigned, task, last_pointed=False):
        self.pid = pid
        self.space_assigned = space_assigned
        self.task = task
        self.last_pointed = last_pointed

    def __str__(self):
        if self.task is None:
            return f'Particion {self.pid} de {self.space_assigned}Kb libre / puntero: {self.last_pointed}'
        else:
            return f'Particion {self.pid} Ocupada con {self.task} / puntero: {self.last_pointed}'

    def __eq__(self, other):
        if isinstance(other, Partition):
            return self.pid == other.pid
        return False

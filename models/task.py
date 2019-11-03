class Task:
    def __init__(self, name, space_requested, time_requested):
        self.name = name
        self.space_requested = int(space_requested)
        self.time_requested = int(time_requested)
        self.loaded = False
        self.init_time = 0

    def __str__(self):
        return f'{self.name} {self.space_requested} Kb'

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.name == other.name
        return False


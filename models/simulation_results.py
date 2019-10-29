class SimulationResults:
    def __init__(self):
        self.tasks_return_time = 0
        self.normalized_return_time = 0
        self.external_fragmentation_ix = 0

    def calculate_normalized_return_time(self, service_time):
        self.normalized_return_time = self.tasks_return_time / service_time

    def increment_external_fragmentation(self, quantity):
        self.external_fragmentation_ix += quantity

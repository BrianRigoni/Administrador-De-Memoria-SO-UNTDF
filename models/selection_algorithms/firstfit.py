from .iselectionalgorithm import ISelectionAlgorithm
from ..partition import Partition


class FirstFit(ISelectionAlgorithm):
    def __init__(self):
        pass

    def get_partition(self, task, memory):
        print('FirstFit ejecutando seleccion de particion')
        for partition in memory.partitions:
            if partition.space_assigned >= task.space_requested:
                new_partition = Partition(task.space_requested, task)
                # memory.create_partition_wtask(new_partition, partition)
                print('FirstFit encontro lugar')
                return True
        print('FirstFit no fue capaz de encontrar particion')
        return False


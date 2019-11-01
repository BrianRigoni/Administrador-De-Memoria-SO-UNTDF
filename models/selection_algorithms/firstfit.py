from .iselectionalgorithm import ISelectionAlgorithm
from ..partition import Partition


class FirstFit(ISelectionAlgorithm):
    def __init__(self):
        pass

    def get_partition(self, task, memory):
        print('FirstFit ejecutando seleccion de particion')
        for idx, partition in enumerate(memory.partitions):
            if (partition.task == None) and (partition.space_assigned >= task.space_requested):
                new_partition = Partition(pid=idx, space_assigned=task.space_requested, task=task)
                print('FirstFit encontro lugar')
                return new_partition
        print('FirstFit no fue capaz de encontrar particion')
        return None


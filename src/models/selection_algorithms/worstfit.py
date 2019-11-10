from .iselectionalgorithm import ISelectionAlgorithm
from ..partition import Partition


class WorstFit(ISelectionAlgorithm):
    def __init__(self):
        pass

    def get_partition(self, task, memory):
        print('WorstFit ejecutando seleccion de particion')
        possibles_partitions = []
        for idx, partition in enumerate(memory.partitions):
            if (partition.task is None) and (partition.space_assigned >= task.space_requested):
                possibles_partitions.append(partition)
        try:
            part = possibles_partitions[0]
        except IndexError:
            part = None
        for partition in possibles_partitions[1:]:
            if partition.space_assigned > part.space_assigned:
                part = partition
        return part
 
from .iselectionalgorithm import ISelectionAlgorithm
from ..partition import Partition


class WorstFit(ISelectionAlgorithm):
    def __init__(self):
        pass

    def get_partition(self, task, memory):
        print('WorstFit ejecutando seleccion de particion')
        selected_partition = None
        for idx, partition in enumerate(memory.partitions):
            if (partition.task == None) and (partition.space_assigned >= task.space_required) and (partition.space_assigned > selected_partition.space_assigned):
                    selected_partition = partition
                    selected.partition.pid = idx
        return selected_partition if selected_partition else None
 
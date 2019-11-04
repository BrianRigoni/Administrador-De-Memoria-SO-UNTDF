from .iselectionalgorithm import ISelectionAlgorithm


class NextFit(ISelectionAlgorithm):
    pointer = 0

    def __init__(self):
        pass

    def get_partition(self, task, memory):
        print('NextFit ejecutando seleccion de particion')
        for partition in memory.partitions[self.pointer:]:
            if (partition.task is None) and (partition.space_assigned >= task.space_requested):
                print('NextFit encontro lugar')
                return partition
        print('NextFit no fue capaz de encontrar particion')
        return None



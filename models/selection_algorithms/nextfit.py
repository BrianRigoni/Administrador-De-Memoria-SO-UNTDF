from .iselectionalgorithm import ISelectionAlgorithm


class NextFit(ISelectionAlgorithm):

    def __init__(self):
        self.pointer = 0

    def get_partition(self, task, memory):
        print('NextFit ejecutando seleccion de particion')
        iterations = 0
        print('Puntero de nextfit se encuentra en ', memory.partitions[self.pointer])
        while iterations < len(memory.partitions):
            partition = memory.partitions[self.pointer]
            if (partition.task is None) and (partition.space_assigned >= task.space_requested):
                print('NextFit encontro lugar')
                return partition
            # Reset del idx para recorrer particiones
            if self.pointer == len(memory.partitions)-1:
                self.pointer = 0
            else:
                self.pointer += 1
            iterations+=1
        print('NextFit no fue capaz de encontrar particion')
        return None



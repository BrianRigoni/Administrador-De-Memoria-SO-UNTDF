from .iselectionalgorithm import ISelectionAlgorithm

class NextFit(ISelectionAlgorithm):

    def __init__(self):
        self.pointer = 0

    # Precondicion: Siempre que se llega a esta funcion hay una sola
    #               Particion con la marca de ultimo apuntado
    def get_pointer(self, partitions):
        for idx, partition in enumerate(partitions):
            if partition.last_pointed:
                self.pointer = idx
                break

    def get_partition(self, task, memory):
        print('NextFit ejecutando seleccion de particion')
        iterations = 0
        if self.pointer >= len(memory.partitions):
            print("Self pointer", self.pointer)
            print("Indice no apunta correctamente debido a concatenacion de particiones")
            self.get_pointer(memory.partitions)
            print("Self pointer desp get", self.pointer)

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



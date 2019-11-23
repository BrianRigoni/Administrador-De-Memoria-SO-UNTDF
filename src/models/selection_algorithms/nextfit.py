from .iselectionalgorithm import ISelectionAlgorithm
from file_writer import FileWriter

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

    def get_partition(self, task, memory, file_writer: FileWriter):
        file_writer.write_content('NextFit ejecutando seleccion de particion')
        iterations = 0
        if self.pointer >= len(memory.partitions):
            self.get_pointer(memory.partitions)


        file_writer.write_content('Puntero de nextfit se encuentra en ' + memory.partitions[self.pointer].__str__())
        while iterations < len(memory.partitions):
            partition = memory.partitions[self.pointer]
            if (partition.task is None) and (partition.space_assigned >= task.space_requested):
                file_writer.write_content('NextFit encontro lugar')
                return partition
            # Reset del idx para recorrer particiones
            if self.pointer == len(memory.partitions)-1:
                self.pointer = 0
            else:
                self.pointer += 1
            iterations+=1
        file_writer.write_content('NextFit no fue capaz de encontrar particion')
        return None



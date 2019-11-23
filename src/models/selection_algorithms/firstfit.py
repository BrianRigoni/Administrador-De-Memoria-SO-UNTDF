from .iselectionalgorithm import ISelectionAlgorithm
from ..partition import Partition
from file_writer import FileWriter


class FirstFit(ISelectionAlgorithm):
    def __init__(self):
        pass

    def get_partition(self, task, memory, file_writer: FileWriter):
        file_writer.write_content('FirstFit ejecutando seleccion de particion')
        for idx, partition in enumerate(memory.partitions):
            if (partition.task is None) and (partition.space_assigned >= task.space_requested):
                file_writer.write_content('FirstFit encontro lugar')
                return partition # Con la primera que encuentra ya retorna la particion sobre la cual asignar
        file_writer.write_content('FirstFit no fue capaz de encontrar particion')
        return None


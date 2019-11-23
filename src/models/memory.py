from .partition import Partition
from file_writer import FileWriter

class Memory:
    def __init__(self, space):
        self.space = space
        self.partitions = []
        # Inicialmente la memoria es una particion del tamano completo
        partition = Partition(pid=0, space_assigned=space, task=None)
        self.partitions.append(partition)

    # Se recibe una lista de tareas que ya terminaron
    # A partir de esa lista se ubica que particiones ocupaban
    # Cuando se encuentra la tarea se le asigna None a la particion
    def release_partitions(self, tasks, file_writer: FileWriter):
        for partition in self.partitions:
            if partition.task in tasks:
                partition.task = None
        self.defrag(file_writer)

    # Luego de liberar particiones
    # Recorro aquellas particiones que tienen None y sean contiguas
    # Para agruparlas en una misma particion
    def defrag(self, file_writer: FileWriter):
        new_partitions = []
        oldp_idx = 0
        newp_idx = 0
        # Recorro todas las particiones ubicando aquellas
        # que no tengan tareas y sean contiguas
        file_writer.write_content('Defragmentador iniciando')
        while oldp_idx < len(self.partitions):
            file_writer.write_content('Deframentando...')
            partition = self.partitions[oldp_idx]
            if partition.task is not None:
                partition.pid = newp_idx
                file_writer.write_content('(Defrag) Copia de particion ocupada ' + partition.__str__())
                new_partitions.append(partition)
                oldp_idx += 1
            else:
                file_writer.write_content('(Defrag) Copia de particion libre ' + partition.__str__()) 
                new_part = Partition(pid=newp_idx, space_assigned=partition.space_assigned, task=None)
                if partition.last_pointed:
                    new_part.last_pointed = True
                found_takenp = False
                while (not found_takenp) and (oldp_idx < len(self.partitions)):
                    oldp_idx += 1
                    try:
                        partition2 = self.partitions[oldp_idx]
                    except IndexError:
                        file_writer.write_content("(Defrag) Ultima particion libre")
                        oldp_idx += 1
                        break
                    if partition2.task is not None:
                        found_takenp = True
                        file_writer.write_content('(Defrag) Fin de None contiguo')
                    else:
                        if partition2.last_pointed:
                            new_part.last_pointed = True
                        new_part.space_assigned += partition2.space_assigned
                new_partitions.append(new_part)
            newp_idx += 1
        # Asignacion de la nueva memoria a la anterior
        self.partitions = new_partitions

    def create_partition_wtask(self, task, selected_partition):
        new_partitions = []
        idx = 0
        for partition in self.partitions:
            if partition != selected_partition:
                # Siempre que sea una posicion que no es donde tiene que ir la tarea
                # Se copia a una nueva lista
                new_partition = Partition(pid=idx, space_assigned=partition.space_assigned, 
                                            task=partition.task, last_pointed=partition.last_pointed)
                new_partitions.append(new_partition)
            else:
                # Cuando se encontro la particion donde iria la tarea
                # Se crea la particion que la tendra y se verifica 
                # Si se debe crear una particion qeu seria el espacio que 
                # No ocuparia la tarea
                remainder = partition.space_assigned - task.space_requested
                partition_w_task = Partition(pid=idx, space_assigned=task.space_requested, task=task, last_pointed=partition.last_pointed)
                new_partitions.append(partition_w_task)
                if remainder > 0:
                    idx += 1
                    free_partition = Partition(pid=idx, space_assigned=remainder, task=None)
                    new_partitions.append(free_partition)
            idx += 1
        self.partitions = new_partitions

    def fix_pointers(self, partition: Partition, file_writer: FileWriter):
        self.print_memory(file_writer)
        for p in self.partitions:
            # Se desmarca la anterior
            if p.last_pointed:
                p.last_pointed = False
            if p == partition:
                p.last_pointed = True
        self.print_memory(file_writer)

    def get_empty_space(self):
        space = 0
        for partition in self.partitions:
            if partition.task is None:
                space += partition.space_assigned
        return space

    def print_memory(self, file_writer: FileWriter):
        file_writer.write_content("------------------Memoria-------------------")
        for partition in self.partitions:
            file_writer.write_content(partition.__str__())
        file_writer.write_content("--------------------------------------------")

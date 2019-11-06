from .partition import Partition


class Memory:
    def __init__(self, space):
        print('Memoria creada')
        self.space = space
        self.partitions = []
        # Inicialmente la memoria es una particion del tamano completo
        partition = Partition(pid=0, space_assigned=space, task=None)
        self.partitions.append(partition)

    # Se recibe una lista de tareas que ya terminaron
    # A partir de esa lista se ubica que particiones ocupaban
    # Cuando se encuentra la tarea se le asigna None a la particion
    # Y se verifican los espacios contiguos
    def release_partition(self, task):
        new_partitions = []
        for idx, partition in enumerate(self.partitions):
            if partition.task == task:
                partition.task = None
                new_partition = Partition(pid=idx, space_assigned=partition.space_assigned, task=None)
                left_part = self.partitions[idx-1] if (self.partitions[idx-1].task is None) else None
                right_part = self.partitions[idx+1] if (self.partitions[idx+1].task is None) else None
                if left_part:
                    new_partition.space_assigned += left_part.space_assigned
                if right_part:
                    new_partition.space_assigned += right_part.space_assigned
                new_partitions.append(new_partition)
            else:
                new_partitions.append(partition)
        self.partitions = new_partitions

    def create_partition_wtask(self, task, selected_partition):
        new_partitions = []
        idx = 0
        for partition in self.partitions:
            if partition != selected_partition:
                # Siempre que sea una posicion que no es donde tiene que ir la tarea
                # Se copia a una nueva lista
                new_partition = Partition(pid=idx, space_assigned=partition.space_assigned, task=partition.task)
                new_partitions.append(new_partition)
            else: 
                # Cuando se encontro la particion donde iria la tarea
                # Se crea la particion que la tendra y se verifica 
                # Si se debe crear una particion qeu seria el espacio que 
                # No ocuparia la tarea
                remainder = partition.space_assigned - task.space_requested
                partition_w_task = Partition(pid=idx, space_assigned=task.space_requested, task=task)
                new_partitions.append(partition_w_task)
                if remainder > 0:
                    idx += 1
                    free_partition = Partition(pid=idx, space_assigned=remainder, task=None)
                    new_partitions.append(free_partition)
            idx += 1
        self.partitions = new_partitions

    def print_memory(self):
        print("------------------Memoria-------------------")
        for partition in self.partitions:
            print(partition)
        print("--------------------------------------------")

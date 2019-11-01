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
    def release_partitions(self, tasks):
        for partition in self.partitions:
            if partition.task in tasks:
                partition.task = None
        self.defrag()

    # Luego de liberar particiones
    # Recorro aquellas particiones que tienen None y sean contiguas
    # Para agruparlas en una misma particion
    def defrag(self):
        pass

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
        self.print_memory()


    def print_memory(self):
        for idx, partition in enumerate(self.partitions):
            print(idx, partition)
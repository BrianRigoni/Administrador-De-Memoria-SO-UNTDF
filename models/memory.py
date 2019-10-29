from .partition import Partition


class Memory:
    def __init__(self, space):
        print('Memoria creada')
        self.space = space
        self.partitions = []
        # Inicialmente la memoria es una particion del tamano completo
        partition = Partition(space, None)
        self.partitions.append(partition)

    # Se recibe una lista de tareas que ya terminaron
    # A partir de esa lista se ubica que particiones ocupaban
    # Cuando se encuentra la tarea se vuelve None
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

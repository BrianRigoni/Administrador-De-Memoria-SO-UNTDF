from .memory import Memory
from .simulation_results import SimulationResults


class MemoryManager:

    def __init__(self, selection_algorithm, tasks, memory_qty, selection_time, assignation_time, release_time):
        print('Administrador de Memoria creado')
        # Variables que son designados por el usuario
        self.selection_algorithm = selection_algorithm
        self.memory_qty = memory_qty
        self.selection_time = selection_time
        self.assignation_time = assignation_time
        self.release_time = release_time
        self.tasks = tasks
        # Variables que son para la simulacion
        self.memory = Memory(space=memory_qty)
        self.results = SimulationResults()
        self.executing = []
        self.finished = []


    def print_tasks(self):
        print("-------------TAREAS POR EJECUTAR-------------")
        for task in self.tasks:
            print(task)
        print("--------------------------------------------")

    def print_executing_tasks(self):
        print("-------------TAREAS EJECUTANDO-------------")
        for task in self.executing:
            print(task)
        print("--------------------------------------------")

    def print_finished_tasks(self):
        print("-------------TAREAS FINALIZADAS-------------")
        for task in self.finished:
            print(task)
        print("--------------------------------------------")
    
    # Simulacion principal del administrador de memoria
    def execute_tasks(self):
        print('-------------COMIENZO SIMULACION-------------')
        time = 0
        # Mientras haya procesos cargados se itera
        while self.tasks or self.executing:
            print(f'Tiempo: {time}')
            # Primero se verifican las tareas que podrian haber terminado
            # Para liberar sus particiones y defragmentar
            self.check_finished_tasks(time)
            print('Memoria despues de defragmentar')
            self.memory.print_memory()
            # Siguiente tarea por ejecutar
            self.print_tasks()
            next_task = self.tasks[0]
            print(f'Siguiente tarea a ubicar: {next_task}')
            partition = self.selection_algorithm.get_partition(next_task, self.memory)

            # Si se pudo ubicar la tarea en memoria, se ubica en executing y se borra de
            # los procesos que faltan cargar
            if partition:
                print(f'Comienza tarea: {next_task} en tiempo {time}')
                next_task.init_time = time
                self.memory.create_partition_wtask(next_task, partition) 
                self.executing.append(self.tasks.pop(self.tasks.index(next_task)))
                self.print_executing_tasks()
                print('Memoria despues de insertar tarea')
                self.memory.print_memory()
            else:
                print(f'No se encontro lugar para tarea: {next_task}')
                print('Memoria despues de intentar insertar tarea')
                self.memory.print_memory()
            time += 1
        # Cuando ya no quedan mas tareas se calculan los resultados
        self.calculate_results()

    # Verifica los lugares que fueron ocupados y luego se desocuparon para defragmentar
    def check_finished_tasks(self, time):
        print('Liberando memoria')
        finished_tasks = []
        for task in self.executing:
            # Si termino su tiempo se saca de executing
            # Y se inserta en finished
            if time == (task.time_requested + task.init_time):
                finished_tasks.append(task)
                self.finished.append(self.executing.pop(self.executing.index(task)))
        # En base a las tareas terminadas, se liberan las particiones correspondientes
        if finished_tasks:
            self.memory.release_partitions(finished_tasks)
        self.print_finished_tasks()

    # Calcula los resultados de la simulacion
    def calculate_results(self):
        print('Calculando resultados')
        pass

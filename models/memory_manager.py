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
    
    def print_executing_tasks(self):
        print("-------------TAREAS EJECUTANDO-------------")
        for task in self.executing:
            print(task)
    
    def print_finished_tasks(self):
        print("-------------TAREAS FINALIZADAS-------------")
        for task in self.finished:
            print(task)
    
    # Simulacion principal del administrador de memoria
    def execute_tasks(self):
        print('-------------COMIENZO SIMULACION-------------')
        time = 0
        # Mientras haya procesos cargados se itera
        while self.tasks:
            print(f'Tiempo: {time}')
            # Primero se verifican las tareas que pueden haber terminado
            # Para liberar sus particiones y defragmentar
            self.check_finished_tasks(time)
            # Siguiente tarea por ejecutar
            self.print_tasks()
            next_task = self.tasks[0]
            print(f'Siguiente tarea a ubicar: {next_task}')
            allocated = self.selection_algorithm.get_partition(next_task, self.memory)
            # Si se pudo ubicar la tarea en memoria, se ubica en executing y se borra de
            # los procesos que faltan cargar
            if allocated:
                print(f'Comienza tarea: {next_task}')
                next_task.init_time = time
                self.executing.append(self.tasks.pop(self.tasks.index(next_task)))
                self.print_executing_tasks()
            else:
                print(f'No se encontro lugar para tarea: {next_task}')
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

    # Utiliza la clase encargada de seleccionar donde se ubicara la tarea a ejecutar
    # Y retorna true o false en base al exito de la funcion
    def allocate_task(self, task):
        print('Ubicando tarea')
        position = self.selection_algorithm.get_position(task)
        if position:
            print(f'{task} sera ubicada en: {position}')
            return True
        else:
            print(f'{task} no pudo ser ubicada en memoria')
            return False

    # Calcula los resultados de la simulacion
    def calculate_results(self):
        print('Calculando resultados')
        pass

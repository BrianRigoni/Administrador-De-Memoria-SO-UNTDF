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
        self.executing = []
        self.finished = []
        self.time = 0
        # Resultados simulacion
        # La fragmentacion externa se calcula en cada instancia de tiempo
        # hasta que se ejecuto la ultima tarea, por lo cual, se calcula
        # mientras se esta en tiempo de seleccion/asignacion/liberacion
        self.external_fragmentation_idx = 0
        self.return_time = 0

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

    def increment_external_fragmentation(self):
        self.external_fragmentation_idx += self.memory.get_empty_space()
        print(f"Tiempo {self.time} / Fragmentacion Externa: {self.external_fragmentation_idx}")

    # Simulacion principal del administrador de memoria
    def execute_tasks(self):
        print('-------------COMIENZO SIMULACION-------------')
        # Mientras haya procesos cargados se itera
        while self.tasks or self.executing:
            print(f'Tiempo: {self.time}')
            # Primero se verifican las tareas que podrian haber terminado
            # Para liberar sus particiones y defragmentar
            self.check_finished_tasks()
            print('Memoria previo a intento de insercion de tarea')
            self.memory.print_memory()
            # Siguiente tarea por ejecutar
            self.print_tasks()
            if self.tasks:
                next_task = self.tasks[0]
                print(f'Siguiente tarea a ubicar: {next_task}')
                print(f'(Tiempo de seleccion) {self.selection_time}')
                # Cuando se esta escogiendo la particion, se debe sumar la fragmentacion
                # que existe en ese tiempo actual (tseleccion)
                self.increment_external_fragmentation()
                self.time += self.selection_time
                partition = self.selection_algorithm.get_partition(next_task, self.memory)
                # Si se pudo ubicar la tarea en memoria, se ubica en executing y se borra de
                # los procesos que faltan cargar
                if partition:
                    print(f'(Tiempo de asignacion) {self.assignation_time}')
                    self.increment_external_fragmentation()
                    self.time += self.assignation_time
                    next_task.init_time = self.time
                    # Cuando se esta insertando la tarea se debe calcular el indice de fragmentacion externa 
                    self.memory.create_partition_wtask(next_task, partition) 
                    self.executing.append(self.tasks.pop(self.tasks.index(next_task)))
                    print(f'Comienza tarea: {next_task} en tiempo {self.time}')
                    self.increment_external_fragmentation()
                    next_task.loaded = True
                    self.print_executing_tasks()
                    print('Memoria despues de insertar tarea')
                    self.memory.print_memory()
                else:
                    # Si no se encontro lugar de igual modo se debe calcular el indice de fragmentacion externa
                    self.increment_external_fragmentation()
                    print(f'No se encontro lugar para tarea: {next_task}')
                    print('Memoria despues de intentar insertar tarea')
                    self.memory.print_memory()
            self.time += 1
        # Cuando ya no quedan mas tareas se calculan los resultados
        self.return_time = self.time - 2
        self.calculate_results()

    # Verifica los lugares que fueron ocupados y luego se desocuparon para defragmentar
    def check_finished_tasks(self):
        print('Liberando memoria')
        finished_tasks = []
        for task in self.executing:
            # Si termino su tiempo se saca de executing
            # Y se inserta en finished
            if self.time >= (task.time_requested + task.init_time):
                finished_tasks.append(task)
                print('Termino ', task)
                # Calculo tiempo de retorno normalizado Ttotal / Tservicio
                total_time = self.time - task.init_time + self.assignation_time + self.selection_time
                print(f"Tiempo total: {total_time}")
                print(f"Tiempo servicio: {task.time_requested}")
                task.normalized_return_time = total_time / task.time_requested
                print(f'Tiempo retorno normalizado: {task.normalized_return_time}')
                self.finished.append(task)
        # En base a las tareas terminadas, se liberan las particiones correspondientes
        if finished_tasks:
            print('Terminaron tareas => Deframentar')
            self.memory.release_partitions(finished_tasks)
            for task in finished_tasks:
                print(task)
                for i in range(self.release_time):
                    # Tiempo de liberacion mientras se debe saber la fragmentacion en ese instante
                    # Ademas, **solo se calcula si todavia hay tareas por ejecutar**
                    if self.tasks:
                        self.increment_external_fragmentation()
                        if len(finished_tasks) > 1:
                            extra = 0
                            last_task_space = finished_tasks[len(finished_tasks)-1].space_requested
                            for task2 in finished_tasks:
                                extra += abs(last_task_space - task2.space_requested)
                            self.external_fragmentation_idx -= extra
                    self.time += 1
                print(f'(Tiempo de liberacion) {self.release_time} => Tiempo actual: {self.time}')
                self.executing.remove(task)

        self.print_finished_tasks()

    # Calcula los resultados de la simulacion
    def calculate_results(self):
        print('Calculando resultados')
        print(f'Tiempo de retorno de la tanda: {self.return_time}')
        print(f'Indice de fragmentacion externa: {self.external_fragmentation_idx}')
        print('Tiempos de retorno normalizados para cada tarea: ')
        for task in self.finished:
            print(f'    * {task}: {task.normalized_return_time}')

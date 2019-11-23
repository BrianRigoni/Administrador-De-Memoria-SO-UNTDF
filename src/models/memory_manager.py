from .memory import Memory
from .simulation_results import SimulationResults
from .selection_algorithms import NextFit
from file_writer import FileWriter

class MemoryManager:

    def __init__(self, selection_algorithm, tasks, memory_qty, selection_time, assignation_time, release_time):
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

    def print_tasks(self, file_writer: FileWriter):
        file_writer.write_content("-------------TAREAS POR EJECUTAR-------------")
        for task in self.tasks:
            file_writer.write_content(task.__str__())
        file_writer.write_content("--------------------------------------------")

    def print_executing_tasks(self, file_writer: FileWriter):
        file_writer.write_content("-------------TAREAS EJECUTANDO-------------")
        for task in self.executing:
            file_writer.write_content(task.__str__())
        file_writer.write_content("--------------------------------------------")

    def print_finished_tasks(self, file_writer: FileWriter):
        file_writer.write_content("-------------TAREAS FINALIZADAS-------------")
        for task in self.finished:
            file_writer.write_content(task.__str__())
        file_writer.write_content("--------------------------------------------")

    def increment_external_fragmentation(self, file_writer: FileWriter):
        self.external_fragmentation_idx += self.memory.get_empty_space()
        file_writer.write_content(f"Tiempo {self.time} / Fragmentacion Externa: {self.external_fragmentation_idx}")

    # Simulacion principal del administrador de memoria
    def execute_tasks(self, file_writer):
        file_writer.write_content('-------------COMIENZO SIMULACION-------------')
        # Mientras haya procesos cargados se itera
        while self.tasks or self.executing:
            file_writer.write_content(f'Tiempo: {self.time}')
            # Primero se verifican las tareas que podrian haber terminado
            # Para liberar sus particiones y defragmentar
            self.check_finished_tasks(file_writer)
            file_writer.write_content('Memoria previo a intento de insercion de tarea')
            self.memory.print_memory(file_writer)
            # Siguiente tarea por ejecutar
            self.print_tasks(file_writer)
            if self.tasks:
                next_task = self.tasks[0]
                file_writer.write_content(f'Siguiente tarea a ubicar: {next_task}')
                file_writer.write_content(f'(Tiempo de seleccion) {self.selection_time}')
                # Cuando se esta escogiendo la particion, se debe sumar la fragmentacion
                # que existe en ese tiempo actual (tseleccion)
                if self.selection_time > 0:
                    self.time += self.selection_time
                    self.increment_external_fragmentation(file_writer)
                partition = self.selection_algorithm.get_partition(next_task, self.memory, file_writer)
                # Solo se corrigen punteros cuando es NextFit
                if type(self.selection_algorithm) is NextFit:
                    file_writer.write_content("Particion encontrada: ", partition)
                    self.memory.fix_pointers(partition, file_writer)

                # Si se pudo ubicar la tarea en memoria, se ubica en executing y se borra de
                # los procesos que faltan cargar
                if partition:
                    file_writer.write_content(f'(Tiempo de asignacion) {self.assignation_time}')
                    # Cuando se esta insertando la tarea se debe calcular el indice de fragmentacion externa 
                    if self.assignation_time > 0:
                        self.increment_external_fragmentation(file_writer)
                        self.time += self.assignation_time
                    next_task.init_time = self.time
                    self.memory.create_partition_wtask(next_task, partition) 
                    self.executing.append(self.tasks.pop(self.tasks.index(next_task)))
                    file_writer.write_content(f'Comienza tarea: {next_task} en tiempo {self.time}')
                    self.increment_external_fragmentation(file_writer)
                    next_task.loaded = True
                    self.print_executing_tasks(file_writer)
                    file_writer.write_content('Memoria despues de insertar tarea')
                    self.memory.print_memory(file_writer)
                else:
                    # Si no se encontro lugar de igual modo se debe calcular el indice de fragmentacion externa
                    self.increment_external_fragmentation(file_writer)
                    file_writer.write_content(f'No se encontro lugar para tarea: {next_task}')
                    file_writer.write_content('Memoria despues de intentar insertar tarea')
                    self.memory.print_memory(file_writer)
            self.time += 1
        # Cuando ya no quedan mas tareas se calculan los resultados
        self.return_time = self.time - 2
        self.calculate_results(file_writer)

    # Verifica los lugares que fueron ocupados y luego se desocuparon para defragmentar
    def check_finished_tasks(self, file_writer: FileWriter):
        file_writer.write_content('Liberando memoria')
        finished_tasks = []
        for task in self.executing:
            # Si termino su tiempo se saca de executing
            # Y se inserta en finished
            if self.time >= (task.time_requested + task.init_time):
                finished_tasks.append(task)
                file_writer.write_content('Termino ' + task.__str__())
                # Calculo tiempo de retorno normalizado Ttotal / Tservicio
                total_time = self.time - task.init_time + self.assignation_time + self.selection_time
                file_writer.write_content(f"Tiempo total: {total_time}")
                file_writer.write_content(f"Tiempo servicio: {task.time_requested}")
                task.normalized_return_time = total_time / task.time_requested
                file_writer.write_content(f'Tiempo retorno normalizado: {task.normalized_return_time}')
                self.finished.append(task)
        # En base a las tareas terminadas, se liberan las particiones correspondientes
        if finished_tasks:
            file_writer.write_content('Terminaron tareas => Deframentar')
            self.memory.release_partitions(finished_tasks, file_writer)
            for task in finished_tasks:
                file_writer.write_content(task.__str__())
                for i in range(self.release_time):
                    # Tiempo de liberacion mientras se debe saber la fragmentacion en ese instante
                    # Ademas, **solo se calcula si todavia hay tareas por ejecutar**
                    if self.tasks:
                        self.increment_external_fragmentation(file_writer)
                        if len(finished_tasks) > 1:
                            extra = 0
                            last_task_space = finished_tasks[len(finished_tasks)-1].space_requested
                            for task2 in finished_tasks:
                                extra += abs(last_task_space - task2.space_requested)
                            self.external_fragmentation_idx -= extra
                    self.time += 1
                file_writer.write_content(f'(Tiempo de liberacion) {self.release_time} => Tiempo actual: {self.time}')
                self.executing.remove(task)

        self.print_finished_tasks(file_writer)

    # Calcula los resultados de la simulacion
    def calculate_results(self, file_writer: FileWriter):
        file_writer.write_content('Calculando resultados')
        file_writer.write_content(f'Tiempo de retorno de la tanda: {self.return_time}')
        file_writer.write_content(f'Indice de fragmentacion externa: {self.external_fragmentation_idx}')
        file_writer.write_content('Tiempos de retorno normalizados para cada tarea: ')
        for task in self.finished:
            file_writer.write_content(f'    * {task.__str__()}: {task.normalized_return_time}')

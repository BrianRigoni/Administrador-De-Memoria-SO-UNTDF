from models import (Task, MemoryManager, BestFit, NextFit,
                    WorstFit, FirstFit)


# Declaracion de variables
PATH_TO_FILE = './datasets/dataset1.txt'
# Campos para instanciar el administrador de memoria
tasks = []
selection_algorithm = FirstFit() # Cambiar por cualquier estrategia de seleccion
selection_time = 1
assignation_time = 1
release_time = 1
memory_qty = 150


# PARA CARGA DE DATASET
# Obtiene el contenido de un archivo

def get_file_contents(file_path):
    file = open(file_path, "r")
    contents = file.readlines()
    file.close()
    return contents


# En base al archivo leido, instancia las tareas
def fill_tasks(data):
    print("-------------CARGANDO DATASET-------------")
    tasks = []
    for line in data:
        splitted_values = line.split(',')
        task_name = splitted_values[0]
        task_space = splitted_values[1]
        task_time = splitted_values[2]
        tasks.append(Task(name=task_name, space_requested=task_space, time_requested=task_time))
    return tasks 


if __name__ == "__main__":
    file_contents = get_file_contents(PATH_TO_FILE)
    tasks = fill_tasks(file_contents)
    for i, task in enumerate(tasks):
        print(i, task)
    print("-------------DATASET CARGADO-------------")
    manager = MemoryManager(selection_algorithm=selection_algorithm, tasks=tasks, memory_qty=memory_qty, selection_time=selection_time, assignation_time=assignation_time, release_time=release_time)
    manager.execute_tasks()

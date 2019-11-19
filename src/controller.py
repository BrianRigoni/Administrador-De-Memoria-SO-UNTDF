from models import Task

class Controller:

    def __init__(self):
        pass

    def get_file_contents(self, file_path):
        file = open(file_path, "r")
        contents = file.readlines()
        file.close()
        return contents


    # En base al archivo leido, instancia las tareas
    def fill_tasks(self, data):
        print("-------------CARGANDO DATASET-------------")
        tasks = []
        for line in data:
            splitted_values = line.split(',')
            task_name = splitted_values[0]
            task_space = splitted_values[1]
            task_time = splitted_values[2]
            task = Task(name=task_name, space_requested=task_space, time_requested=task_time)
            tasks.append(task)
            print(task)
        return tasks


if __name__ == "__main__":
    controller = Controller()
    file_contents = controller.get_file_contents('dataset1.txt')
    tasks = controller.fill_tasks(file_contents)

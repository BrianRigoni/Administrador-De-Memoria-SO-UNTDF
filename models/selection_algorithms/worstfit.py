from .iselectionalgorithm import ISelectionAlgorithm


class WorstFit(ISelectionAlgorithm):
    def __init__(self):
        pass

    def get_partition(self, task, memory):
        print('WorstFit ejecutando seleccion de particion')

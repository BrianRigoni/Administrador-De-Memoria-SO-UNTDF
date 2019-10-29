from .iselectionalgorithm import ISelectionAlgorithm


class BestFit(ISelectionAlgorithm):
    def __init__(self):
        pass

    def get_partition(self, task, memory):
        print('BestFit ejecutando seleccion de particion')

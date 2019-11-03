from .iselectionalgorithm import ISelectionAlgorithm


class NextFit(ISelectionAlgorithm):
    pointer = 0

    def __init__(self):
        pass

    def get_partition(self, task, memory):
        print('NextFit ejecutando seleccion de particion')


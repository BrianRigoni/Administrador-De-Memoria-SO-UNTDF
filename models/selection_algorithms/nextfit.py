from .iselectionalgorithm import ISelectionAlgorithm


class NextFit(ISelectionAlgorithm):
    def __init__(self):
        pass

    def get_partition(self, task, memory):
        print('NextFit ejecutando seleccion de particion')

class FileWriter:
    def __init__(self):
        # Se crea el archivo
        self.file_name = "resultados_simulacion.txt"
        self.file = open(self.file_name, "w")
        self.file.write("Simulacion de Administrador de Memoria")
        self.file.close()

    def write_content(self, content):
        self.file.open(self.file_name, "a+")
        self.write(content)
        self.close()

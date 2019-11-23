class FileWriter:
    def __init__(self):
        # Se crea el archivo
        self.file_name = "resultados_simulacion.txt"
        file = open(self.file_name, "w")
        file.write("Simulacion de Administrador de Memoria \n")
        file.close()

    def write_content(self, content):
        file = open(self.file_name, "a+")
        file.write(content+"\n")
        file.close()

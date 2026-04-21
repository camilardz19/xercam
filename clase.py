class Capibara:
    def __init__(self, nombre, edad, peso, color, habitat):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__color = color
        self.__habitat = habitat
    
    
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_peso(self):
        return self.__peso

    def get_color(self):
        return self.__color

    def get_habitat(self):
        return self.__habitat
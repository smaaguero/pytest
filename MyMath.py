class MyMath:

#Crear tests.
#Bajamer imagen de jenkin modificada.
#Ejecutar docker dentro de docker.
#Crear jobs
#

    import math

    @staticmethod
    def sum (a,b):
        """
        Suma dos numeros
        :param a: Primer elemento de la suma
        :param b: Segundo elemento de la suma
        :return: La suma de los dos elementos
        """
        return a + b

    @staticmethod
    def substract (a,b):
        """
        Resta dos numeros
        :param a: Primer elemento de la suma
        :param b: Segundo elemento de la suma
        :return: La resta de los dos elementos
        """
        return a - b

    @staticmethod
    def mult(e,b):
        """
        Multiplica dos elementos
        :param e: Primer elemento de la multiplicacion
        :param b: Segundo elemento de la multiplicacion
        :return: La multiplicacion de los dos elementos
        """
        return e*b

    @staticmethod
    def div(e,b):
        """
        Divide dos elementos
        :param e: Primer elemento de la multiplicacion
        :param b: Segundo elemento de la multiplicacion
        :return: La division de los dos elementos
        """
        return e/b

    @staticmethod
    def squareroot(a):
        """
        Ejecuta la raiz de un elemnto
        :param a: Elemento de la raiz cuadrada
        :return: La raiz del elemento
        """
        return  math.sqrt(a)

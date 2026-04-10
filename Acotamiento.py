import math

class FaseAcotamiento:

    def __init__(self, x0, delta, funcion):
        self.x0 = x0
        self.delta = delta
        self.funcion = funcion

    def encontrar_intervalo(self):

        x0 = self.x0
        delta = self.delta
        f = self.funcion

        # evaluar valores iniciales
        f0 = f(x0)
        f1 = f(x0 + delta)
        f_1 = f(x0 - delta)

        # decidir dirección
        if f_1 >= f0 and f0 >= f1:
            pass
        elif f_1 <= f0 and f0 <= f1:
            delta = -delta
        else:
            return (x0 - delta, x0 + delta)

        k = 0
        x_prev = x0
        x_actual = x0 + delta
        f_actual = f(x_actual)

        while True:
            paso = (2 ** k) * delta
            x_next = x_actual + paso
            f_next = f(x_next)

            # si empieza a subir, ya tenemos el intervalo
            if f_next > f_actual:
                return (x_prev, x_next)

            x_prev = x_actual
            x_actual = x_next
            f_actual = f_next
            k += 1


def prueba(nombre, funcion, x0, delta):
    metodo = FaseAcotamiento(x0, delta, funcion)
    intervalo = metodo.encontrar_intervalo()

    print(nombre)
    print("intervalo:", intervalo)
    print()


if __name__ == "__main__":

    # funcion exponencial
    prueba(
        "f(x) = e^x - 5x",
        lambda x: math.exp(x) - 5*x,
        0,
        0.5
    )

    # funcion polinomial
    prueba(
        "f(x) = x^4 - 3x^3 + 2",
        lambda x: x**4 - 3*x**3 + 2,
        0,
        0.1
    )

    # funcion logaritmica
    prueba(
        "f(x) = x^2 - ln(x)",
        lambda x: x**2 - math.log(x),
        0.5,
        0.2
    )
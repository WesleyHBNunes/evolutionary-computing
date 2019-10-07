from clonalg import *
import matplotlib.pyplot as plt
import statistics


def grafico(plot_data):
    plt.plot(plot_data[0], label="CLONALG")

    plt.legend()
    plt.title("Resultados CLONALG")
    plt.savefig("chart.svg")


def main():
    result = []
    for i in range(10):
        result.append(clonalg())

    data = [result]

    print("Dados CLONALG")
    print("Media: " + str(statistics.mean(result)))
    print("Mediana: " + str(statistics.median(result)))
    print("Desvio Padrão: " + str(statistics.stdev(result, None)))

    grafico(data)


if __name__ == '__main__':
    main()

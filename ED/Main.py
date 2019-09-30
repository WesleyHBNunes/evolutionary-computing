from ed_basico import *
import matplotlib.pyplot as plt
import statistics


def grafico(plot_data):
    plt.plot(plot_data[0], label="ED básico")
    plt.legend()
    plt.title("Comparação entre ED")
    plt.savefig("chart.svg")


def main():
    plot_basico = []
    for i in range(10):
        plot_basico.append(ed_basico())

    data = [plot_basico]
    print("Dados ED básico")
    print("Media: " + str(statistics.mean(plot_basico)))
    print("Mediana: " + str(statistics.median(plot_basico)))
    print("Desvio Padrão: " + str(statistics.stdev(plot_basico, None)))
    grafico(data)


if __name__ == "__main__":
    main()

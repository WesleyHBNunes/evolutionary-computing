import matplotlib.pyplot as plt
import statistics
import TLBO


def grafico(plot_data):
    plt.plot(plot_data, label="TLBO")
    plt.title("Gráfico TLBO")
    plt.legend()
    plt.savefig("chart.svg")


def main():
    plot = []

    for i in range(5):
        result = TLBO.tlbo()
        plot.append(result)

    print("Dados TLBO")
    print("Media: " + str(statistics.mean(plot)))
    print("Mediana: " + str(statistics.median(plot)))
    print("Desvio Padrão: " + str(statistics.stdev(plot, None)))
    grafico(plot)


if __name__ == '__main__':
    main()

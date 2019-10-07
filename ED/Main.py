from ed_basico import *
from ed_rand import *
from ed_best import *
from ed_basico_aprend_opo import *
import matplotlib.pyplot as plt
import statistics


def grafico(plot_data):
    plt.plot(plot_data[0], label="ED básico")
    plt.plot(plot_data[1], label="ED Rand")
    plt.plot(plot_data[2], label="ED aprendizado oposição")
    plt.plot(plot_data[3], label="ED best")
    plt.legend()
    plt.title("Comparação entre ED")
    plt.savefig("chart.svg")


def main():
    plot_basico = []
    plot_rand = []
    plot_best = []
    plot_basico_aprend = []
    print('======= BÁSICO ===========')
    for i in range(100):
        plot_basico.append(ed_basico_aprend(1))
        if i % 10 == 0:
            print(i)

    print('======== RAND ===========')
    for i in range(100):
        plot_rand.append(ed_rand())
        if i % 10 == 0:
            print(i)

    print('========= BEST ========')
    for i in range(100):
        plot_basico_aprend.append(ed_basico_aprend(0.7))
        if i % 10 == 0:
            print(i)

    print('=========== APREND ============')
    for i in range(100):
        plot_best.append(ed_best())
        if i % 10 == 0:
            print(i)

    data = [plot_basico, plot_rand, plot_basico_aprend, plot_best]

    print("Dados ED básico")
    print("Media: " + str(statistics.mean(plot_basico)))
    print("Mediana: " + str(statistics.median(plot_basico)))
    print("Desvio Padrão: " + str(statistics.stdev(plot_basico, None)))

    print("Dados ED Rand")
    print("Media: " + str(statistics.mean(plot_rand)))
    print("Mediana: " + str(statistics.median(plot_rand)))
    print("Desvio Padrão: " + str(statistics.stdev(plot_rand, None)))

    print("Dados ED básico Aprendizado oposição")
    print("Media: " + str(statistics.mean(plot_basico_aprend)))
    print("Mediana: " + str(statistics.median(plot_basico_aprend)))
    print("Desvio Padrão: " + str(statistics.stdev(plot_basico_aprend, None)))

    print("Dados ED Best")
    print("Media: " + str(statistics.mean(plot_best)))
    print("Mediana: " + str(statistics.median(plot_best)))
    print("Desvio Padrão: " + str(statistics.stdev(plot_best, None)))

    grafico(data)


if __name__ == "__main__":
    main()

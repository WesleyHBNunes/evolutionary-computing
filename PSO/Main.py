from PSO.PSO_basico import pso_basico
from PSO.PSO_constricao import pso_constricao
from PSO.PSO_inercia import pso_inercia
import matplotlib.pyplot as plt
import statistics


def grafico(plot_data):
    plt.plot(plot_data[0], label="PSO básico")
    plt.plot(plot_data[1], linewidth=3, linestyle='dashed', label="PSO com fator de constrição", markersize=2)
    plt.plot(plot_data[2], label="PSO com fator de inércia", markersize=12)
    plt.title("Comparação entre PSO")
    plt.legend()
    plt.savefig("chart.svg")

def main():
    plot_data_basico = []
    plot_data_constricao = []
    plot_data_inercia = []

    for i in range(100):
        result_basico = pso_basico()
        plot_data_basico.append(result_basico.fitness.values[0])

    for i in range(100):
        result_constricao = pso_constricao()
        plot_data_constricao.append(result_constricao.fitness.values[0])

    for i in range(100):
        result_inercia = pso_inercia()
        plot_data_inercia.append(result_inercia.fitness.values[0])

    data = []
    data.append(plot_data_basico)
    data.append(plot_data_constricao)
    data.append(plot_data_inercia)

    print("Dados PSO básico")
    print("Media: " + str(statistics.mean(plot_data_basico)))
    print("Mediana: " + str(statistics.median(plot_data_basico)))
    print("Desvio Padrão: " + str(statistics.stdev(plot_data_basico, None)))
    print()
    print("Dados PSO com fator de constrição")
    print("Media: " + str(statistics.mean(plot_data_constricao)))
    print("Mediana: " + str(statistics.median(plot_data_constricao)))
    print("Desvio Padrão: " + str(statistics.stdev(plot_data_constricao, None)))
    print()
    print("Dados PSO com fator de inércia")
    print("Media: " + str(statistics.mean(plot_data_inercia)))
    print("Mediana: " + str(statistics.median(plot_data_inercia)))
    print("Desvio Padrão: " + str(statistics.stdev(plot_data_inercia, None)))
    grafico(data)


if __name__ == "__main__":
    main()
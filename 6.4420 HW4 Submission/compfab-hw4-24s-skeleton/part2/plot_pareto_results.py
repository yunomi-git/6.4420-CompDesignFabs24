import pandas as pd
import paths
import os
import matplotlib.pyplot as plt


def plot_3_2():
    result_dir = os.path.join(paths.HOME_PATH, '..', 'data', 'assignment5', 'results', 'part2')
    pareto_path = os.path.join(result_dir, 'q2_result.csv')
    all_path = os.path.join(result_dir, 'q2_all_perfs.csv')

    pareto_data = pd.read_csv(pareto_path)
    all_data = pd.read_csv(all_path)

    plt.plot(pareto_data['x'], pareto_data['y'], color='m')
    plt.scatter(all_data['x'], all_data['y'])
    plt.ylabel("Compliance")
    plt.xlabel("Mass")
    plt.show()

def plot_3_1():
    result_dir = os.path.join(paths.HOME_PATH, '..', 'data', 'assignment5', 'result', 'part2')
    pareto_path = os.path.join(result_dir, 'q1_result.csv')

    pareto_data = pd.read_csv(pareto_path)

    plt.plot(pareto_data['x'], pareto_data['y'], color='m')
    plt.ylabel("y")
    plt.xlabel("x")
    plt.show()

if __name__=="__main__":
    plot_3_1()

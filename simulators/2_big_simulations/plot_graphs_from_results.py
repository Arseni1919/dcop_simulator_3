from simulators.plots.collisions_vs_iters import *
from simulators.plots.coverage_vs_iters import *


def main():
    # file_name = '11.07.2021-06:21:44_10T-20R_50Bi-5Si_50PRBLMS_.results'
    file_name = '19.07.2021-21:59:01_10T-20R_25Bi-8Si_50PRBLMS_.results'


    file_name = f'results/{file_name}'

    plot_coverage_vs_iters(file_name)
    plot_collisions_vs_iters(file_name)


if __name__ == '__main__':
    main()















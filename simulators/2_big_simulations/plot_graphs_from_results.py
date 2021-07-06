from simulators.plots.collisions_vs_iters import *
from simulators.plots.coverage_vs_iters import *


def main():
    file_name = '06.07.2021-14:18:14_10T-7R_5Bi-4Si_5PRBLMS_.results'
    file_name = f'results/{file_name}'

    plot_coverage_vs_iters(file_name)
    plot_collisions_vs_iters(file_name)


if __name__ == '__main__':
    main()















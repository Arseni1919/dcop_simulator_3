from simulators.plots.collisions_vs_iters import *
from simulators.plots.coverage_vs_iters import *


def main():
    file_name = '07.07.2021-15:57:34_7T-10R_10Bi-5Si_5PRBLMS_.results'
    file_name = f'results/{file_name}'

    plot_coverage_vs_iters(file_name)
    plot_collisions_vs_iters(file_name)


if __name__ == '__main__':
    main()















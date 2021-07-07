from simulators.plots.collisions_vs_iters import *
from simulators.plots.coverage_vs_iters import *


def main():
    file_name = '07.07.2021-13:13:16_7T-10R_5Bi-10Si_3PRBLMS_.results'
    file_name = f'results/{file_name}'

    plot_coverage_vs_iters(file_name)
    plot_collisions_vs_iters(file_name)


if __name__ == '__main__':
    main()















from simulators.plots.collisions_vs_iters import *
from simulators.plots.coverage_vs_iters import *


def main():
    file_name = '25.07.2021-01:08:51_10T-20R_20Bi-8Si_50PRBLMS_complex.results'
    # file_name = '24.07.2021-15:19:18_10T-20R_20Bi-8Si_50PRBLMS_grid.results'

    file_name = f'results/{file_name}'

    plot_coverage_vs_iters(file_name)
    plot_collisions_vs_iters(file_name)


if __name__ == '__main__':
    main()















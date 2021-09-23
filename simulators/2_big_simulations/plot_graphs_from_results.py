from simulators.plots.collisions_vs_iters import *
from simulators.plots.coverage_vs_iters import *


def main():
    # file_name = '25.07.2021-01:08:51_10T-20R_20Bi-8Si_50PRBLMS_complex.results'
    # file_name = '24.07.2021-15:19:18_10T-20R_20Bi-8Si_50PRBLMS_grid.results'
    # file_name = '26.08.2021-19:39:38_20T-30R_20Bi-8Si_50PRBLMS_targets_apart_grid.results'
    # file_name = '27.08.2021-12:44:18_20T-30R_20Bi-8Si_50PRBLMS_targets_apart_complex.results'
    # file_name = '2021.09.14-15:50:09_20T-30R_20Bi-8Si_50PRBLMS_targets_apart_complex.results'
    # file_name = '2021.09.14-16:07:23_20T-30R_20Bi-8Si_50PRBLMS_targets_apart_grid.results'
    file_name = '2021.09.23-14:00:41_20T-30R_20Bi-8Si_50PRBLMS_targets_apart_grid.results'
    file_name = '2021.09.23-14:22:40_20T-30R_20Bi-8Si_50PRBLMS_targets_apart_complex.results'

    file_name = f'results/{file_name}'

    print_t_test(file_name)
    plot_coverage_vs_iters(file_name)
    plot_collisions_vs_iters(file_name)


if __name__ == '__main__':
    main()















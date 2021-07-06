from simulators.constants_and_packages import *


class Tracker:
    def __init__(self):
        self.curr_problem = 0
        self.curr_alg_num = 0
        self.curr_bigger_iteration = 0
        self.curr_smaller_iteration = 0
        self.final = B_NUMBER_OF_PROBLEMS * len(ALGORITHMS_TO_CHECK)
        self.done = 5
        self.biggest = 20

    def step(self, problem, alg_num, curr_bigger_iteration, curr_smaller_iteration=0):
        self.curr_problem = problem
        self.curr_alg_num = alg_num
        self.curr_bigger_iteration = curr_bigger_iteration
        self.curr_smaller_iteration = curr_smaller_iteration
        self._print_progress()

    def _print_progress(self):
        self.done = int(
            self.biggest * (
                    (self.curr_problem * len(ALGORITHMS_TO_CHECK) + self.curr_alg_num + 1)
                    / self.final)
        )
        print(colored(f'\rProblem: ({self.curr_problem + 1}/{B_NUMBER_OF_PROBLEMS}), '
                      f'Alg: ({self.curr_alg_num + 1}/{len(ALGORITHMS_TO_CHECK)}), '
                      f'Iter B: ({self.curr_bigger_iteration + 1}/{B_ITERATIONS_IN_BIG_LOOPS}), '
                      f'Iter S: ({self.curr_smaller_iteration}/{B_ITERATIONS_IN_SMALL_LOOPS}), '
                      f'Progress: [{"#" * self.done}{"." * (self.biggest - self.done)}]', 'green'), end='')


tracker = Tracker()

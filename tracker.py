from CONSTANTS import *


class Tracker:
    def __init__(self):
        self.curr_problem = 0
        self.curr_alg_num = 0
        self.curr_bigger_iteration = 0
        self.curr_smaller_iteration = 0
        self.final = NUMBER_OF_PROBLEMS * len(ALGORITHMS_TO_CHECK)
        self.done = 5
        self.biggest = 20

    def update(self, problem, alg_num, iteration):
        self.curr_problem = problem
        self.curr_alg_num = alg_num
        self.curr_bigger_iteration = iteration

    def print_progress(self):
        self.done = int(
            self.biggest * (
                    (self.curr_problem * len(ALGORITHMS_TO_CHECK) + self.curr_alg_num + 1)
                    / self.final)
        )
        print(colored(f'\rProblem: ({self.curr_problem + 1}/{NUMBER_OF_PROBLEMS}), '
                      f'Alg: ({self.curr_alg_num + 1}/{len(ALGORITHMS_TO_CHECK)}), '
                      f'Iter B: ({self.curr_bigger_iteration + 1}/{ITERATIONS_IN_BIG_LOOPS}), '
                      f'Iter S: ({self.curr_smaller_iteration}/{ITERATIONS_IN_SMALL_LOOPS}), '
                      f'Progress: [{"#" * self.done}{"." * (self.biggest - self.done)}]', 'green'), end='')


tracker = Tracker()

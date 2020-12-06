# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from CONSTANTS import *
from main_help_functions import *
from algorithms import *
from pygame_part import *


def main():
    clock, screen, finish_sound = init_pygame()

    for problem in range(NUMBER_OF_PROBLEMS):
        print_main(description='The problem', order=problem, pred='#'*30)
        all_sprites, all_agents = init_problem(problem)
        time.sleep(2)

        for alg_name, params in algorithms_to_check:
            collisions_counter = 0
            print_main(description='The algorithm', order=alg_name, pred='#'*10)
            algorithm = get_the_algorithm(alg_name)
            go_back_to_initial_positions(all_sprites, all_agents, screen)

            for i in range(ITERATIONS):
                print_main('Iteration in a bigger loop', i+1, pred='#')
                new_positions, collisions = algorithm(params=params, all_agents=all_agents)
                collisions_counter += collisions
                # new_positions = None
                blit_pygame(screen, all_sprites, new_positions)

            print(colored(f'Collisions in {alg_name}: {collisions_counter}', 'yellow'))

    close_pygame(finish_sound)
    pickle_results_if()
    plot_results_if()


if __name__ == '__main__':
    main()


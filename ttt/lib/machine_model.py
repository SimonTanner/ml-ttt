import copy, random, json, os
from ttt.lib.db_tree_accessor import DbAccessor

class MachinePlayer():

    global states

    def __init__(self):
        self.states = [[1, 1.0 / 9.0], [2, 1.0 / 9.0], [3, 1.0 / 9.0], [4, 1.0 / 9.0], [5, 1.0 / 9.0], [6, 1.0 / 9.0], [7, 1.0 / 9.0], [8, 1.0 / 9.0], [9, 1.0 / 9.0]]
        self.counter = 0
        self.start = '0'
        self.path = '0'
        self.options = list(range(1, 10))
        self.db = DbAccessor()

    def get_states(self, path):
        states = self.db.get_options(path)
        if states != None:
            db_states = []
            for option in states:
                db_states.append([int(option.option), option.value])
                self.states = db_states

    def check_options(self, options):
        chosen_option = [i for i in self.options if i not in options]
        if len(chosen_option) > 0:
            chosen_option = chosen_option[0]
        else:
            chosen_option = None
        return chosen_option


    def update_options_and_states(self, options, machine_choice=None):
        chosen_option = self.check_options(options)
        if chosen_option == None:
            chosen_option = machine_choice
        if chosen_option:
            self.path += str(chosen_option)
            path = self.db.create_path_entry(self.path)
            self.options.remove(chosen_option)
            self.get_states(self.path)
            states = self.states
            [states.remove(option) for option in states if option[0] == chosen_option]
            self.states = states
            for option in self.options:
                self.db.create_choice_entry(path, str(option))

    def choose_option(self, options):
        self.update_options_and_states(options)
        self.get_states(self.path)
        states = self.states
        state_options = list(map(lambda x: x[0], states))
        states = [i for i in states if i[0] in options]
        max_chance = max(states, key=lambda x: x[1])[1]
        choices = []
        for i in states:
            if i[1] / max_chance < 10:
                try:
                    options.index(i[0])
                    choices.append(i[0])
                except (ValueError, IndexError):
                    continue

        choice = random.choice(choices)
        self.update_options_and_states(self.options, choice)

        return choice

    def game_won(self, options=None):
        if options:
            self.update_options_and_states(options)

        for index in range(0, len(self.path) - 1):
            choice = str(self.path[index + 1])
            current_path = self.path[0:(index + 1)]
            print(current_path)
            addition = 1.0 / (9.0 - index)
            print(self.db.get_choice(current_path, self.db.get_options(current_path), choice))
            current_value = self.db.get_choice(current_path, self.db.get_options(current_path), choice).value + addition
            self.db.update_choice_entry(current_path, choice, current_value)
            options = self.db.get_options(current_path)
            total = sum(list(map(lambda option: option.value, options)))
            for option in options:
                new_value = option.value / total
                self.db.update_choice_entry(current_path, option.option, new_value)

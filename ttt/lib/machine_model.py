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
        print('path : ' + str(10 - len(self.path)) + ' options: ' + str(len(options)))
        chosen_option = self.check_options(options)
        print('chosen option = ' + str(chosen_option))
        if chosen_option == None:
            chosen_option = machine_choice
            print('Mac choice = ' + str(machine_choice))
        if chosen_option:
            self.path += str(chosen_option)
            path = self.db.create_path_entry(self.path)
            self.options.remove(chosen_option)
            self.get_states(self.path)
            states = self.states
            [states.remove(option) for option in states if option[0] == chosen_option]
            print('states = ' + str(states))
            self.states = states
            for option in self.options:
                self.db.create_choice_entry(path, str(option))

    def choose_option(self, options):
        self.update_options_and_states(options)
        self.get_states(self.path)
        states = self.states
        print(states)
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
        print('Machine choice = ' + str(choice))
        #self.options.remove(choice)
        #self.path = self.path + str(choice)
        self.update_options_and_states(self.options, choice)

        return choice

    def game_won(self):
        for i in range(0, len(self.path)-1):
            index = int(i)
            choice = int(self.path[index + 1])
            index_2 = list(map(lambda x: x[0], self.tree[self.path[0:(index + 1)]])).index(choice)
            branch = (self.tree[self.path[0:(index + 1)]])
            self.tree[self.path[0:(index + 1)]][index_2][1] = 1.0 / (len(self.path) - i) + self.tree[self.path[0:(index + 1)]][index_2][1]
            total = sum(list(map(lambda x: x[1], self.tree[self.path[0:(index + 1)]])))

            for v in branch:
                v[1] = v[1] / total

        self.close_tree_data()
        self.path = '0'

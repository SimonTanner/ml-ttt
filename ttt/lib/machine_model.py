import copy, random, json, os

class MachinePlayer():

    global states

    def __init__(self):
        self.states = [[1, 1.0 / 9.0], [2, 1.0 / 9.0], [3, 1.0 / 9.0], [4, 1.0 / 9.0], [5, 1.0 / 9.0], [6, 1.0 / 9.0], [7, 1.0 / 9.0], [8, 1.0 / 9.0], [9, 1.0 / 9.0]]
        self.counter = 0
        self.start = '0'
        self.path = '0'
        self.options = list(range(1, 10))
        self.dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/tree_data.json')
        self.create_data()


    def create_data(self):
        if os.path.isfile(self.dir_path):
            with open(self.dir_path, 'r') as data:
                tree = json.load(data)
                self.tree = json.loads(tree)
                data.close()
        else:
            self.tree = {}
            self.create_tree()
            self.grow_tree(self.start, self.states)


    def create_tree(self):
        self.tree[self.start] = self.states[:]

    def grow_tree(self, start, states):
        tree = self.tree

        for i in range(0, len(states)):
            new_states = states[:]
            key = start + str(new_states.pop(i)[0])
            if len(new_states) > 0:
                tree[key] = copy.deepcopy(new_states)

            self.grow_tree(key, new_states)

        self.tree = tree

    def check_options(self, options):
        if 10 - len(self.path) != len(options):
            path = [i for i in self.options if i not in options]
            path = path[0]
            self.path += str(path)
            self.options.remove(path)

    def choose_option(self, options):
        self.check_options(options)

        states = self.tree[self.path]
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
        self.options.remove(choice)
        self.path = self.path + str(choice)

        return choice

    def close_tree_data(self):
        with open(self.dir_path, 'w') as data:
            tree = json.dumps(self.tree)
            json.dump(tree, data)
            data.close()

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

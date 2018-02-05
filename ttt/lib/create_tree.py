import copy
from ttt.models import *

class CreateTreeData():

    def __init__(self):
        self.states = [[1, 1.0 / 9.0], [2, 1.0 / 9.0], [3, 1.0 / 9.0], [4, 1.0 / 9.0], [5, 1.0 / 9.0], [6, 1.0 / 9.0], [7, 1.0 / 9.0], [8, 1.0 / 9.0], [9, 1.0 / 9.0]]
        self.start = '0'
        self.tree = {}
        self.path = '0'
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

    def populate_db(self):
        for path, data in self.tree.items():
            db_path = MachinePath(id=path)
            db_path.save()
            for options in data:
                db_choice = MachineChoice(option=str(options[0]), value = options[1], path = db_path)
                db_choice.save()

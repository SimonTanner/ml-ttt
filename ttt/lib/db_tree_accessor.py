from ttt.models import *

class DbAccessor():

    def get_path(self, path):
        try:
            machine_path = MachinePath.objects.get(id=path)
        except Exception:
            machine_path = None
        return machine_path


    def get_options(self, path):
        try:
            machine_options = MachineChoice.objects.filter(path=path)
        except Exception:
            machine_options = None
        return machine_options

    def get_choice(self, path, options, choice):
        try:
            machine_choice = options.get(option=choice)
        except Exception:
            machine_choice = None
        return machine_choice

    def create_path_entry(self, path):
        if self.get_path(path) == None:
            new_path = MachinePath(id=path)
            new_path.save()

    def create_choice_entry(self, path, choice, value):
        if self.get_options(path) == None:
            new_option = MachineChoice(option=choice, value=value, path=path)
            new_option.save()
        else:
            options = self.get_options(path)
            if self.get_choice(path, options, choice) == None:
                new_choice = MachineChoice(option=choice, value=value, path=path)
                new_choice.save()

    def update_choice_entry(self, path, choice, value):
        options = self.get_options(path)
        choice = self.get_choice(path, options, choice)
        choice.value = value
        choice.save()

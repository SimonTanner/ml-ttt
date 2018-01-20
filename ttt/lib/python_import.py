import importlib.machinery, os

def import_python(file_name, function_name):

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

    mod = importlib.machinery.SourceFileLoader(function_name, path)

    function = mod.load_module(function_name)

    return(function)

from plugins.core.base_model import db
from pathlib import Path


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PluginManager(metaclass=SingletonMeta):
    def __init__(self, app) -> None:
        self.app = app

    def add_moudles(self):
        models = []
        #Работает на серваке для выгрузки 
        paths = [str(x).split('/')[-1] for x in Path('./plugins').iterdir() if x.is_dir()]
        #Работает на локалхосте
        #paths = [str(x).split('\\')[-1] for x in Path('.\plugins').iterdir() if x.is_dir()]
        for path in paths:
            if path == 'core':
                continue
            model = __import__(f'plugins.{path}.models') # plugons
            model = getattr(model, f'{path}') # module_name
            __import__(f'plugins.{path}.routers')
            model = getattr(model, 'models') # models
            models.append(getattr(model, path.title()))

        db.connect()
        db.create_tables(models)

    def route(self, rule: str, **options):
        def decorator(function):
            return self.app.route(rule, **options)(function)
        return decorator

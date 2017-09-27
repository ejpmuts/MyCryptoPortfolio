# config


class Configuration(object):
    DATABASE = {
        'name': 'main.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    DEBUG = False
    SECRET_KEY = 'Rm0GxEfEn7k0pnQFinuh3YcJnQKm2gz6PRyAnETIWqbn0ecQlEjlGavk4UmTlJLt'


class DevelopConfiguration(Configuration):
    DEBUG = True

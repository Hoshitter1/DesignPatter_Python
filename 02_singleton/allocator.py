class Database:
    """__init__ gets called, which is not something we want"""
    _instance = None

    def __init__(self):
        print('__init__ gets called whatever you do...')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print('new instance')
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)

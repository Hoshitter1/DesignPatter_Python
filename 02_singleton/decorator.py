def singleton(cls_):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls_ not in instances.keys():
            instances[cls_] = cls_(*args, **kwargs)
        return instances[cls_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('this should not be called more than once')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)

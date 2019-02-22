class Resource:
    __value = 0

    def reset(self):
        self.__value = 0

    def set_value(self, number):
        self.__value = number

    def get_value(self):
        return self.__value


class ObjectPool:
    __instance = None
    __resources = list()

    def __init__(self):
        if ObjectPool.__instance is not None:
            raise NotImplemented("This is a singleton class.")

    @staticmethod
    def get_instance():
        if ObjectPool.__instance is None:
            ObjectPool.__instance = ObjectPool()

        return ObjectPool.__instance

    def get_resource(self):
        if len(self.__resources) > 0:
            print("Using existing resource.")
            return self.__resources.pop(0)
        else:
            print("Creating new resource.")
            return Resource()

    def return_resource(self, resource):
        resource.reset()
        self.__resources.append(resource)


def main():
    pool = ObjectPool.get_instance()

    # Testing
    one = pool.get_resource()
    two = pool.get_resource()

    one.set_value(10)
    two.set_value(20)

    print("%s = %d" % (one, one.get_value()))
    print("%s = %d" % (two, two.get_value()))

    pool.return_resource(one)
    pool.return_resource(two)

    one = None
    two = None

    one = pool.get_resource()
    two = pool.get_resource()
    print("%s = %d" % (one, one.get_value()))
    print("%s = %d" % (two, two.get_value()))


if __name__ == "__main__":
    main()

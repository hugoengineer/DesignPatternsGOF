import random

class __TestSingleton:
    instance = random.randint(1, 1000)
    print(instance)

SingletonInstance = __TestSingleton()

if __name__ == "__main__":
    s1 = SingletonInstance
    s2 = SingletonInstance

    print(f"Instance 1 ID: {id(s1)} with value {s1.instance}")
    print(f"Instance 2 ID: {id(s2)} with value {s2.instance}")
    
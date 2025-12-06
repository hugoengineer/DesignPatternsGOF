from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return"ConcreteImplementationA: resultado da implementação A"


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return"ConcreteImplementationB: resultado da implementação B"


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end="")


if __name__ == "__main__":


    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
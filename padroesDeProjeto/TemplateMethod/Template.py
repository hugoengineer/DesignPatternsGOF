#Esse padrão é uma herança comum mas possui metodos que sao fixos e outro moldaveis e são passados por herança
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
      
    # Métodos concretos que já possuem uma implementação padrão
    def base_operation1(self) -> None:
        print("AbstractClass: Base Operation 1")

    # Métodos abstratos que podem ser reescritos pelas subclasses
    @abstractmethod
    def required_operations1(self) -> None:
        pass


    def hook1(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass1: Implemented Operation 1")

if __name__ == "__main__":
    concrete_class1 = ConcreteClass1()
    concrete_class1.template_method()
from abc import ABC, abstractmethod
class Bear(ABC):
    @abstractmethod
    def constract(self):
        pass
class TeddyBear(Bear):
    def constract(self):
        pass
class PlacticBear(Bear):
    def constract(self):
        pass
class Soldier(ABC):
    @abstractmethod
    def constract(self):
        pass
class PlushSoldier(Soldier):
    def constract(self):
        pass
class PlasticSoldier(Soldier):
    def constract(self):
        pass
class ToyFactory(ABC):
    @abstractmethod
    def createBear(self,a:Bear):
        pass
    @abstractmethod
    def createSoldier(self,a:Soldier):
        pass
class PlasticFactory(ToyFactory):
    def createBear(self,a:Bear):
        pass
    def createSoldier(self,a:Soldier):
        pass
class PlushFactory(ToyFactory):
    def createBear(self,a:Bear):
        pass
    def createSoldier(self,a:Soldier):
        pass
class Client:
    __factory:ToyFactory
    def set_factory(self,factory:ToyFactory):
        self.__factory = factory
    def construct(self):
        pass

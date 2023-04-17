import abc

class Special(abc.ABC):
    
    @abc.abstractmethod
    def __init__(self, fighter) -> None:
        pass
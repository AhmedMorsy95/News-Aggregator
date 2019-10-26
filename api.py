from abc import abstractmethod, ABC


class api(ABC):
    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def list(self):
        pass


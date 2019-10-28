from abc import abstractmethod, ABC


class api(ABC):
    # abstract class which any API added must inherit and implement the abstract methods in it.
    # This way adding a new API can be generic and easy.
    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def list(self):
        pass


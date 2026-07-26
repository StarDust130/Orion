from abc import ABC, abstractmethod


class BaseTool(ABC):
    name: str
    description: str

    @property
    @abstractmethod
    def schema(self) -> dict:
        pass

    @abstractmethod
    async def execute(self, **kwargs) -> str:
        pass

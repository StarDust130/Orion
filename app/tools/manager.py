from app.tools.calculator import CalculatorTool
from app.tools.weather import WeatherTool


class ToolManager:
    def __init__(self):

        self.tools = {
            "calculator": CalculatorTool(),
            "weather": WeatherTool(),
        }

    def schemas(self):

        return [tool.schema for tool in self.tools.values()]

    async def execute(
        self,
        name,
        arguments,
    ):

        tool = self.tools[name]

        return await tool.execute(
            **arguments,
        )

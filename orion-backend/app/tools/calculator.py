import math

from app.tools.base import BaseTool


class CalculatorTool(BaseTool):
    name = "calculator"

    description = "Perform mathematical calculations."

    @property
    def schema(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "Math expression",
                        }
                    },
                    "required": ["expression"],
                },
            },
        }

    async def execute(self, expression: str):
        allowed = {
            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs,
            "round": round,
            "pi": math.pi,
            "e": math.e,
        }

        result = eval(
            expression,
            {"__builtins__": {}},
            allowed,
        )

        return str(result)

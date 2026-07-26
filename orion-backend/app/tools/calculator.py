import math

from base import BaseTool


class CalculatorTool(BaseTool):
    name = "calculator"

    description = "Perform mathematical calculations."

    async def execute(self, expression: str) -> str:
        allowed = {
            "abs": abs,
            "round": round,
            "pow": pow,
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "pi": math.pi,
            "e": math.e,
        }

        try:
            result = eval(
                expression,
                {"__builtins__": {}},
                allowed,
            )

            return str(result)

        except (ValueError, SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            return f"Calculation error: {e}"


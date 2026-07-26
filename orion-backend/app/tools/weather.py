import httpx
from base import BaseTool


class WeatherTool(BaseTool):
    name = "weather"

    description = "Get current weather."

    async def execute(
        self,
        latitude: float,
        longitude: float,
    ) -> str:

        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            "&current=temperature_2m,weather_code"
        )

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        data = response.json()

        current = data["current"]

        return (
            f"Temperature: {current['temperature_2m']}°C\n"
            f"Weather Code: {current['weather_code']}"
        )

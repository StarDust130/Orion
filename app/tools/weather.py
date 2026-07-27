import httpx

from app.tools.base import BaseTool


class WeatherTool(BaseTool):
    name = "weather"

    description = "Get current weather."

    @property
    def schema(self):
        return {
            "type": "function",
            "function": {
                "name": "weather",
                "description": "Get current weather.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "City name"},
                    },
                    "required": ["city"],
                },
            },
        }

    async def execute(
        self,
        city: str,
    ) -> str:

        async with httpx.AsyncClient() as client:
            geocode = await client.get(
                "https://geocoding-api.open-meteo.com/v1/search",
                params={"name": city, "count": 1},
            )
            geocode.raise_for_status()
            results = geocode.json().get("results", [])
            if not results:
                return f"I couldn't find a location named {city}."
            location = results[0]
            url = (
                "https://api.open-meteo.com/v1/forecast"
                f"?latitude={location['latitude']}"
                f"&longitude={location['longitude']}"
                "&current=temperature_2m,weather_code"
            )
            response = await client.get(url)
            response.raise_for_status()

        data = response.json()

        current = data["current"]

        return (
            f"Temperature: {current['temperature_2m']}°C\n"
            f"Weather Code: {current['weather_code']}"
        )

from fastapi import FastAPI
import requests

from ranking import rank_notifications


app = FastAPI()


TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJwYXVscmFqbWVzc2lAZ21haWwuY29tIiwiZXhwIjoxNzc4MDQ3OTI0LCJpYXQiOjE3NzgwNDcwMjQsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiI3MjFkZWU0MS00NWFiLTRlMGItYmMyZS02MTFhNGQyMzJjMTQiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJwYXVscmFqIHMiLCJzdWIiOiJjYjFlOWJkNS1jM2IzLTQwZmEtOGI2Yi0wYzExMWNjYjhmNzQifSwiZW1haWwiOiJwYXVscmFqbWVzc2lAZ21haWwuY29tIiwibmFtZSI6InBhdWxyYWogcyIsInJvbGxObyI6IjIxMTcyMzAwNzAxMDAiLCJhY2Nlc3NDb2RlIjoiQlRDRHFUIiwiY2xpZW50SUQiOiJjYjFlOWJkNS1jM2IzLTQwZmEtOGI2Yi0wYzExMWNjYjhmNzQiLCJjbGllbnRTZWNyZXQiOiJOQVJZQU55Z0hySmtIc1JUIn0.BIbevKv2Gmx9tasxovObMQX8Fk1AOZaYJ55BcNbnCBA"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}


@app.get("/")
def home():

    return {
        "message": "Notification Backend Running"
    }


@app.get("/notifications")
def notifications():

    url = "http://20.207.122.201/evaluation-service/notifications"

    response = requests.get(
        url,
        headers=headers
    )

    data = response.json()

    print(data)

    # Adjust based on actual API structure
    notifications_data = data.get(
        "notifications",
        []
    )

    ranked = rank_notifications(
        notifications_data
    )

    return {
        "TopNotifications": ranked
    }
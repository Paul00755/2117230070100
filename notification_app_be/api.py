import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJwYXVscmFqbWVzc2lAZ21haWwuY29tIiwiZXhwIjoxNzc4MDQ2MTY5LCJpYXQiOjE3NzgwNDUyNjksImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiIyYmUxYWIwNy0yNGU4LTRhYjctOGI2Ni1kMjgwZjczYThhZDQiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJwYXVscmFqIHMiLCJzdWIiOiJjYjFlOWJkNS1jM2IzLTQwZmEtOGI2Yi0wYzExMWNjYjhmNzQifSwiZW1haWwiOiJwYXVscmFqbWVzc2lAZ21haWwuY29tIiwibmFtZSI6InBhdWxyYWogcyIsInJvbGxObyI6IjIxMTcyMzAwNzAxMDAiLCJhY2Nlc3NDb2RlIjoiQlRDRHFUIiwiY2xpZW50SUQiOiJjYjFlOWJkNS1jM2IzLTQwZmEtOGI2Yi0wYzExMWNjYjhmNzQiLCJjbGllbnRTZWNyZXQiOiJOQVJZQU55Z0hySmtIc1JUIn0.ZWeJkNe925r5gOcIW1zA7gLsPPWB-zNRFCb97Yfj7w4"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}


def fetch_notifications():

    url = "http://20.207.122.201/evaluation-service/notifications"

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()
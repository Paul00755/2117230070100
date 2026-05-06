#import
import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJwYXVscmFqbWVzc2lAZ21haWwuY29tIiwiZXhwIjoxNzc4MDQ0NjE5LCJpYXQiOjE3NzgwNDM3MTksImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiI0NmNkMTI5Ny1iMGJmLTQ5OTAtODIyNy1jZWQ3MjY3MTRmNTgiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJwYXVscmFqIHMiLCJzdWIiOiJjYjFlOWJkNS1jM2IzLTQwZmEtOGI2Yi0wYzExMWNjYjhmNzQifSwiZW1haWwiOiJwYXVscmFqbWVzc2lAZ21haWwuY29tIiwibmFtZSI6InBhdWxyYWogcyIsInJvbGxObyI6IjIxMTcyMzAwNzAxMDAiLCJhY2Nlc3NDb2RlIjoiQlRDRHFUIiwiY2xpZW50SUQiOiJjYjFlOWJkNS1jM2IzLTQwZmEtOGI2Yi0wYzExMWNjYjhmNzQiLCJjbGllbnRTZWNyZXQiOiJOQVJZQU55Z0hySmtIc1JUIn0.OMbnhDOKBfgPxJr0zE7RmtyD8VqXIVknDjZw4wZMBiY"

LOG_API = "http://20.207.122.201/evaluation-service/logs"

def Log(stack, level, package, message):

    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(
        LOG_API,
        json=payload,
        headers=headers
    )

    return response.json()
import requests


response_1 = requests.post(
    "https://petstore.swagger.io/v2/pet/1/uploadImage",
    json={"petId": 101},
)
response_2 = requests.post(
    "https://petstore.swagger.io/v2/pet",
    json={
        "id": 0,
        "category": {
            "id": 0,
            "name": "string",
        },
        "name": "Basiliy",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 0,
                "name": "string",
            }
        ],
        "status": "available",
    },
)
response_3 = requests.put(
    "https://petstore.swagger.io/v2/pet",
    json={
        "id": 0,
        "category": {
            "id": 0,
            "name": "string",
        },
        "name": "Bobby",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 0,
                "name": "string",
            }
        ],
        "status": "available",
    },
)
response_4 = requests.get(
    "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
)
response_5 = requests.get("https://petstore.swagger.io/v2/pet/101")
response_6 = requests.post(
    "https://petstore.swagger.io/v2/pet/101",
    json={"petId": 101, "status": "pending"},
)
response_7 = requests.delete("https://petstore.swagger.io/v2/pet/101")

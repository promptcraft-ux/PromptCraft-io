import requests
def call_api(endpoint, data):
    try:
        response = requests.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
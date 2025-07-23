import requests

dados = {
    "veiculo_id": 1,
    "latitude": -22.919,
    "longitude": -43.242
}

res = requests.post("http://localhost:5000/localizacao", json=dados)

print(res.status_code)
print(res.json())

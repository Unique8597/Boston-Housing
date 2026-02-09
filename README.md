headers = {"Authorization": f"Bearer {token}"}
payload = {
    "table_name": "msbl.public_partner_bvnupdate",
    "limit": 1000,
    "filters": {
        "last_name": {"value": "Emmanuel"},
        "first_name": {"value": "John"}
    }
}

response = requests.post(f"{Base_Url}/query_data", json=payload, headers=headers)
data = response.json()
print(data)

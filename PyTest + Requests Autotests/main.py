import requests

host = "https://api.pokemonbattle.me:9104"

response = requests.post(
    f"{host}/pokemons",
    json={"name": "generate", "photo": "generate"},
    headers={
        "Content-Type": "application/json",
        "trainer_token": "ba22756233e4bc84746e8ed76efa0564",
    },
)
print(response.json())

response = requests.put(
    f"{host}/pokemons",
    json={
        "pokemon_id": "11067",
        "name": "New Name",
        "photo": "https://dolnikov.ru/pokemons/albums/008.png",
    },
    headers={
        "Content-Type": "application/json",
        "trainer_token": "ba22756233e4bc84746e8ed76efa0564",
    },
)
print(response.json())

response = requests.post(
    f"{host}/trainers/add_pokeball",
    json={"pokemon_id": "11067"},
    headers={
        "Content-Type": "application/json",
        "trainer_token": "ba22756233e4bc84746e8ed76efa0564",
    },
)
print(response.json())

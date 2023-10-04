import requests
import pytest

token = "ba22756233e4bc84746e8ed76efa0564"

host = "https://api.pokemonbattle.me:9104/"


def test_status_code():
    response = requests.get(f"{host}/trainers")
    assert response.status_code == 200


def test_correct_trainer_name():
    response = requests.get(f"{host}/trainers", params={"trainer_id": 1711})
    assert response.json()["trainer_name"] == "Szdlwsk"




from app.models.cat import Cat

def test_get_all_cats_return_empty_list_when_db_is_empty(client):
    # Act
    response = client.get("/cats")

    # Assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_one_cat_returns_seeded_cat(client, one_cat):
    # Act
    response = client.get(f"/cats/{one_cat.id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["name"] == one_cat.name
    assert response_body["personality"] == one_cat.personality
    assert response_body["color"] == one_cat.color

def test_create_cat_happy_path(client):
    EXPECTED_CAT = dict(
        name="Meow",
        personality="loud",
        color="orange"
    )
    # Act
    response = client.post("/cats", json=EXPECTED_CAT)
    response_body = response.get_data(as_text=True)

    actual_cat = Cat.query.get(1)

    # Assert
    assert response.status_code == 201
    assert response_body == f"Cat {EXPECTED_CAT['name']} successfully created"

    assert EXPECTED_CAT["name"] == actual_cat.name
    assert EXPECTED_CAT["personality"] == actual_cat.personality
    assert EXPECTED_CAT["color"] == actual_cat.color
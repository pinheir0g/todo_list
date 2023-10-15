def test_get_task(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert b"tasks" in response.data


def test_add_task(client):
    data = {
        "title": "Tarefa Teste",
        "description": "Testando Tarefa",
        "done": False,
    }
    response = client.post("/tasks", json=data)
    assert response.status_code == 201

    task_data = response.get_json()
    assert task_data["title"] == data["title"]
    assert task_data["description"] == data["description"]
    assert task_data["done"] == data["done"]


def test_edit_task(client):
    data = {
        "title": "Tarefa Teste editada",
        "description": "Testando Tarefa editada",
        "done": True,
        "id": 1
    }
    response = client.put("tasks/1", json=data)
    assert response.status_code == 200

    task_data = response.get_json()
    assert task_data["title"] == data["title"]
    assert task_data["description"] == data["description"]
    assert task_data['done'] is True


def test_get_task_with_id(client):
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert b"title" in response.data


def test_get_task_with_title(client):
    response = client.get('tasks/Tarefa Teste editada')
    assert response.status_code == 200
    assert b"title" in response.data


def test_delete_task(client):
    response = client.delete("tasks/1")
    assert response.status_code == 200
    tasks = client.get("tasks/1")
    assert tasks.status_code == 404

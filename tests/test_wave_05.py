import pytest
from app.models.goal import Goal
from app.db import db


#@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_goals_no_saved_goals(client):
    # Act
    response = client.get("/goals")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


#@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_goals_one_saved_goal(client, one_goal):
    # Act
    response = client.get("/goals")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "title": "Build a habit of going outside daily"
        }
    ]


#@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_goal(client, one_goal):
    # Act
    response = client.get("/goals/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "goal" in response_body
    assert response_body == {
        "goal": {
            "id": 1,
            "title": "Build a habit of going outside daily"
        }
    }


#@pytest.mark.skip(reason="test to be completed by student")
def test_get_goal_not_found(client):
    pass
    # Act
    response = client.get("/goals/1")
    response_body = response.get_json()

    #raise Exception("Complete test")
    # Assert
    assert response.status_code == 404
    assert "message" in response_body
    assert response_body["message"] == "goal 1 not found"
    # ---- Complete Test ----
    # assertion 1 goes here
    # assertion 2 goes here
    # ---- Complete Test ----


#@pytest.mark.skip(reason="No way to test this feature yet")
def test_create_goal(client):
    # Act
    response = client.post("/goals", json={
        "title": "My New Goal"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "goal" in response_body
    assert response_body == {
        "goal": {
            "id": 1,
            "title": "My New Goal"
        }
    }


#@pytest.mark.skip(reason="test to be completed by student")
def test_update_goal(client, one_goal):
    #raise Exception("Complete test")
    # Act
    response = client.put("/goals/1", json={
        "title": "Updated Goal Title",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "goal" in response_body
    assert response_body == {
        "goal": {
            "id": 1,
            "title": "Updated Goal Title",
        }
    }
    goal = db.session.get(Goal, 1)
    assert goal.title == "Updated Goal Title"


#@pytest.mark.skip(reason="test to be completed by student")
def test_update_goal_not_found(client):
    #raise Exception("Complete test")
    # Act
    response = client.put("/goals/1", json={
        "title": "Updated Goal Title",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert "message" in response_body
    assert response_body["message"] == "goal 1 not found"


#@pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_goal(client, one_goal):
    # Act
    response = client.delete("/goals/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {
        "details": 'Goal 1 "Build a habit of going outside daily" successfully deleted'
    }

    # Check that the goal was deleted
    response = client.get("/goals/1")
    response_body = response.get_json()
    assert response.status_code == 404
    assert response_body == {"message": "goal 1 not found"}
    # assert Goal.query.get(1) is None

    #raise Exception("Complete test with assertion about response body")
    # *****************************************************************
    # **Complete test with assertion about response body***************
    # *****************************************************************


#@pytest.mark.skip(reason="test to be completed by student")
def test_delete_goal_not_found(client):
    #raise Exception("Complete test")
    # Act
    response = client.delete("/goals/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert "message" in response_body
    assert response_body == {"message": "goal 1 not found"}
    assert Goal.query.all() == []


#@pytest.mark.skip(reason="No way to test this feature yet")
def test_create_goal_missing_title(client):
    # Act
    response = client.post("/goals", json={})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "details": "Invalid data"
    }

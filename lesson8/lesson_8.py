import pytest
import requests

BASE_URL = "your_api_base_url" 
PROJECTS_ENDPOINT = f"{BASE_URL}/api-v2/projects"

class ProjectPage:
   

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.projects_url = f"{self.base_url}/api-v2/projects"

    def create_project(self, data):
        return requests.post(self.projects_url, json=data)

    def get_project(self, project_id):
        return requests.get(f"{self.projects_url}/{project_id}")

    def update_project(self, project_id, data):
        return requests.put(f"{self.projects_url}/{project_id}", json=data)


@pytest.fixture
def project_page():
    return ProjectPage()


def test_create_project_positive(project_page):
    data = {"name": "Test Project", "description": "Project description"} 
    response = project_page.create_project(data)
    assert response.status_code == 201


def test_create_project_negative(project_page):
    data = {"description": "Project description"} 
    response = project_page.create_project(data)
    assert response.status_code == 400  


def test_get_project_positive(project_page):
    create_data = {"name": "Temp Project", "description": "Temp description"}
    create_response = project_page.create_project(create_data)
    assert create_response.status_code == 201
    project_id = create_response.json()["id"] 

    response = project_page.get_project(project_id)
    assert response.status_code == 200


def test_get_project_negative(project_page):
    response = project_page.get_project("nonexistent_id")
    assert response.status_code == 404 


def test_update_project_positive(project_page):
    create_data = {"name": "Temp Project", "description": "Temp description"}
    create_response = project_page.create_project(create_data)
    assert create_response.status_code == 201
    project_id = create_response.json()["id"] 

    update_data = {"description": "Updated description"}
    response = project_page.update_project(project_id, update_data)
    assert response.status_code == 200


def test_update_project_negative(project_page):
    update_data = {"description": "Updated description"}
    response = project_page.update_project("nonexistent_id", update_data)
    assert response.status_code == 404 

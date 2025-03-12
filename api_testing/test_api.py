import requests 

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200, "Failed to fetch users"
    assert len(response.json()) > 0, "No users returned"

def test_get_albums():
    response = requests.get(f"{BASE_URL}/albums")
    assert response.status_code == 200, "Failed to fetch albums"
    assert len(response.json()) > 0, "No albums returned"

def test_get_photos():
    response = requests.get(f"{BASE_URL}/photos")
    assert response.status_code == 200, "Failed to fetch photos"
    assert len(response.json()) > 0, "No photos returned"

if __name__ == "__main__":
    test_get_users()
    test_get_albums()
    test_get_photos()
    print("All API tests passed!")
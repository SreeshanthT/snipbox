# SnipBox API Documentation

SnipBox is a short note-saving application where users can save snippets, organize them with tags, and manage them through a set of RESTful APIs. This documentation provides details about the available API endpoints, their usage, and examples.

---

## **Authentication APIs**

### **1. Signup API**
- **Endpoint**: `/api/auth/signup/`
- **Method**: `POST`
- **Description**: Allows a new user to create an account.
- **Request Body**:
  ```json
  {
      "username": "testuser",
      "email": "testuser@example.com",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "username": "testuser",
      "email": "testuser@example.com"
  }
  ```

### **2. Login API**
- **Endpoint**: `/api/auth/token/`
- **Method**: `POST`
- **Description**: Authenticates a user and provides an access token and refresh token.
- **Request Body**:
  ```json
  {
      "username": "testuser",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "access": "ACCESS_TOKEN",
      "refresh": "REFRESH_TOKEN"
  }
  ```

### **3. Refresh Token API**
- **Endpoint**: `/api/auth/token/refresh/`
- **Method**: `POST`
- **Description**: Refreshes an access token using the refresh token.
- **Request Body**:
  ```json
  {
      "refresh": "REFRESH_TOKEN"
  }
  ```
- **Response**:
  ```json
  {
      "access": "NEW_ACCESS_TOKEN"
  }
  ```

---

## **Snippet APIs**

### **1. Overview API**
- **Endpoint**: `/api/snippets/overview/`
- **Method**: `GET`
- **Description**: Provides the total count of snippets created by the logged-in user and a list of snippets with hyperlinks to their detail APIs.
- **Response**:
  ```json
  {
      "total_count": 2,
      "snippets": [
          {
              "id": 1,
              "title": "My First Snippet",
              "detail_url": "http://localhost:8000/api/snippets/1/"
          },
          {
              "id": 2,
              "title": "Another Snippet",
              "detail_url": "http://localhost:8000/api/snippets/2/"
          }
      ]
  }
  ```

### **2. Create Snippet API**
- **Endpoint**: `/api/snippets/`
- **Method**: `POST`
- **Description**: Allows the logged-in user to create a new snippet.
- **Request Body**:
  ```json
  {
      "title": "My Snippet",
      "note": "This is a note for the snippet.",
      "tags": [{"title": "Python"}, {"title": "Django"}]
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "title": "My Snippet",
      "note": "This is a note for the snippet.",
      "tags": [{"title": "Python"}, {"title": "Django"}],
      "created_at": "2024-12-06T10:00:00Z",
      "updated_at": "2024-12-06T10:00:00Z"
  }
  ```

### **3. List Snippets API**
- **Endpoint**: `/api/snippets/`
- **Method**: `GET`
- **Description**: Lists all snippets created by the logged-in user.
  - **Response**:
    ```json
    [
      {
        "id": 2,
        "title": "My Snippets",
        "note": "This is a note for the snippet.",
        "created_at": "2024-12-06T09:41:26.794999Z",
        "updated_at": "2024-12-06T09:44:52.314939Z",
        "user": 2,
        "tags": [
          {
            "id": 3,
            "title": "Python"
          },
          {
            "id": 4,
            "title": "Django"
          }
        ]
      }
    ]
    ```

### **4. Detail Snippet API**
- **Endpoint**: `/api/snippets/<id>/`
- **Method**: `GET`
- **Description**: Retrieves the details of a specific snippet created by the logged-in user.
- **Response**:
  ```json
  {
    "id": 2,
    "title": "My Snippets",
    "note": "This is a note for the snippet.",
    "created_at": "2024-12-06T09:41:26.794999Z",
    "updated_at": "2024-12-06T09:44:52.314939Z",
    "user": 2,
    "tags": [
      {
        "id": 3,
        "title": "Python"
      },
      {
        "id": 4,
        "title": "Django"
      }
    ]
  }
  ```

### **5. Update Snippet API**
- **Endpoint**: `/api/snippets/<id>/`
- **Method**: `PUT`
- **Description**: Updates a specific snippet.
- **Request Body**:
  ```json
  {
      "title": "Updated Snippet",
      "note": "This is the updated note for the snippet.",
      "tags": [{"title": "UpdatedTag"}]
  }
  ```
- **Response**:
  ```json
  {
    "id": 2,
    "title": "Updated Snippet",
    "note": "This is the updated note for the snippet.",
    "created_at": "2024-12-06T09:41:26.794999Z",
    "updated_at": "2024-12-06T09:44:52.314939Z",
    "user": 2,
    "tags": [
      {
        "id": 5,
        "title": "UpdatedTag"
      }
    ]
  }
  ```

### **6. Delete Snippet API**
- **Endpoint**: `/api/snippets/<id>/`
- **Method**: `DELETE`
- **Description**: Deletes a specific snippet and returns the updated list of snippets.
- **Response**:
  ```json

  ```

### **7. List Tags API**
- **Endpoint**: `/api/tags/`
- **Method**: `GET`
- **Description**: Lists all tags used by the logged-in user.
- **Response**:
  ```json
  [
      {"id": 1, "title": "Python"},
      {"id": 2, "title": "Django"}
  ]
  ```

### **8. Tag Detail API**
- **Endpoint**: `/api/tags/<id>/`
- **Method**: `GET`
- **Description**: Retrieves all snippets linked to a specific tag.
- **Response**:
  ```json
  {
    "id": 1,
    "title": "Python"
  }
  ```
  
### **9. Tag Linked Snippets API**
- **Endpoint**: `/api/tags/<id>/snippets_by_tag/`
- **Method**: `GET`
- **Description**: Retrieves all snippets linked to a specific tag.
- **Response**:
  ```json
  {
      "title": "Python",
      "snippets": [
          {
              "id": 1,
              "title": "My First Snippet",
              "note": "This is a note for my first snippet.",
              "created_at": "2024-12-06T10:00:00Z",
              "updated_at": "2024-12-06T10:00:00Z"
          }
      ]
  }
  ```
  

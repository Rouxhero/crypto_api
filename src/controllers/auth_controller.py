"""Authentication controller module."""

from flask import request
from src.core.db import DataBaseInstance


class AuthController:
    """Authentication controller class."""

    def __init__(self):
        """Class constructor."""
        self.database = DataBaseInstance
    
    def register(self):
        """Register method."""
        request_data = request.get_json()
        name = request_data.get("name")
        email = request_data.get("email")
        password = request_data.get("password")
        self.database.create_user(name, email, password)
        return "User created successfully!"
    


AuthControllerInstance = AuthController()
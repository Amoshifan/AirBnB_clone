# models/base_model.py

class BaseModel:
    """Base class for all models."""

    def __init__(self, id, name):
        """
        Initialize a new BaseModel instance.

        Args:
            id (int): The ID of the model.
            name (str): The name of the model.
        """
        self.id = id
        self.name = name

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: String representation of the instance.
        """
        return f'BaseModel(id={self.id}, name="{self.name}")'


"""
Exception
"""


class InsectSurvivalException(Exception):
    """Exception raised when an insect does not survive over winter."""
    def __init__(self, insect):
        """
        Exception for insect not surviving over winter
        """
        message = f"{insect.name} did not survive over winter."
        super().__init__(message)

class UnknownError(Exception):
    """Unknown error"""

    def __init__(self, message: str):
        super().__init__(self, message)
        pass

"""
define you excpetions classes here
"""


class InvaildRegister(Exception):
    def __init__(self, message, case) -> None:
        self.message = message
        self.case = case

    def message(self) -> str:
        return self.message


class InvalidLogin(Exception):
    def __init__(self, message, case) -> None:
        self.message = message
        self.case = case

    def message(self) -> str:
        return self.message


class InvalidUserUpdate(Exception):
    def __init__(self, message, case) -> None:
        self.message = message
        self.case = case

    def message(self) -> str:
        return self.message


class InvalidUpdateListing(Exception):
    def __init__(self, message) -> None:
        self.message = message
        # self.case = case


class InvalidListing(Exception):
    """
    This class defines an InvalidListing Exception.
    """

    def __init__(self, message) -> None:
        """
        Exception constructor.
        """
        self.message = message

    # def message(self) -> str:
    #     return self.message


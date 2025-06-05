class UserNotFound(Exception):
    detail = "User not found"

class PasswordIncorrect(Exception):
    detail = "Incorrect password"
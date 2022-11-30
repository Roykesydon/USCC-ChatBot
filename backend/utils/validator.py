import re


class Validator:
    global connection

    def __init__(self):
        self._errors = []

    """
    regular
    """

    def required(self, params):
        if len([x for x in params if x is None]) > 0:
            self._errors.append("Information is incomplete")

    def is_letter_number_only(self, str):
        if re.match("^[A-Za-z0-9]*$", str):
            return True
        return False

    """
    User
    """

    def check_user_id(self, input, letterNumberOnly=True):
        if letterNumberOnly == True and self.is_letter_number_only(input) == False:
            self._errors.append("User ID has illegal characters")
            return

        if input is None or len(input) < 3 or len(input) > 30:
            self._errors.append("User ID does not meet the formatting requirements")

    def check_password(self, input, letterNumberOnly=True):
        if letterNumberOnly == True and self.is_letter_number_only(input) == False:
            self._errors.append("Password has illegal characters")
            return

        if input is None or len(input) < 3 or len(input) > 30:
            self._errors.append("Password does not meet the formatting requirements")

    def get_errors(self):
        return self._errors

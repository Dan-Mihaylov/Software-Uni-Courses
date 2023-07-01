class Profile:

    def __init__(self, username: str, password):
        self.__username = username
        self.__password = password
        self.validate_username()
        self.validate_password()

    def validate_username(self):
        if not 5 <= len(self.__username) <= 15:
            raise ValueError(f"The username must be between 5 and 15 characters.")

    def validate_password(self):
        long = False
        uppercase = False
        digit = False

        count = 0

        for char in self.__password:
            count += 1
            if char.isupper():
                uppercase = True
            elif char.isdigit():
                digit = True

        if count >= 8:
            long = True

        if not all([long, uppercase, digit]):
            raise ValueError(f"The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "pAs_0swrd")
print(correct_profile)


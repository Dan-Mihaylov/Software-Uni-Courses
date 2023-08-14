class DVD:

    def __init__(self, name: str, _id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.is_rented = False
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction

    @staticmethod
    def convert_month_to_string(month: int):
        months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
                  ]
        return months[month - 1]

    @classmethod
    def from_date(cls, _id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split(".")
        month = DVD.convert_month_to_string(int(month))
        return cls(name, _id, int(year), month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"



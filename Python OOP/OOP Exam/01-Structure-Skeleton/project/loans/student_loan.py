from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    _AMOUNT = 2000.0
    _INTEREST_RATE = 1.5

    def __init__(self):
        super().__init__(StudentLoan._INTEREST_RATE, StudentLoan._AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2


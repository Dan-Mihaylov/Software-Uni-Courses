from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    _AMOUNT = 50000.0
    _INTEREST_RATE = 3.5

    def __init__(self):
        super().__init__(MortgageLoan._INTEREST_RATE, MortgageLoan._AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5

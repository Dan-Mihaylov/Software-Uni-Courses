from typing import List
from project.loans.base_loan import BaseLoan
from project.clients.base_client import BaseClient
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:

    _ALLOWED_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    _ALLOWED_CLIENTS = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self._ALLOWED_LOANS:
            raise Exception("Invalid loan type!")

        new_loan = self._ALLOWED_LOANS[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self._ALLOWED_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        new_client = self._ALLOWED_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def _find_loan_by_type(self, loan_type: str):
        for loan in self.loans:
            if loan.type() == loan_type:
                return loan
        return None

    def _find_client_by_id(self, client_id: str):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def grant_loan(self, loan_type: str, client_id: str):
        curr_loan = self._find_loan_by_type(loan_type)
        curr_client = self._find_client_by_id(client_id)

        if ((curr_loan.type() == "StudentLoan" and curr_client.type() == "Adult")
                or (curr_loan.type() == "MortgageLoan" and curr_client.type() == "Student")):
            raise Exception("Inappropriate loan type!")

        self.loans.remove(curr_loan)
        curr_client.loans.append(curr_loan)
        return f"Successfully granted {loan_type} to {curr_client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        found_client = self._find_client_by_id(client_id)
        if found_client is None:
            raise Exception("No such client!")

        if len(found_client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(found_client)
        return f"Successfully removed {found_client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        total_loans_increased = 0

        for loan in self.loans:
            if loan.type() == loan_type:
                loan.increase_interest_rate()
                total_loans_increased += 1

        return f"Successfully changed {total_loans_increased} loans."

    def increase_clients_interest(self, min_rate: float):
        total_clients_increased = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                total_clients_increased += 1

        return f"Number of clients affected: {total_clients_increased}."

    def _get_total_clients_income(self):
        total = 0
        for client in self.clients:
            total += client.income
        return total

    def _get_granted_loans_sum_and_number(self):
        granted = 0
        total_sum = 0
        for client in self.clients:
            if len(client.loans) > 0:
                for loan in client.loans:
                    granted += 1
                    total_sum += loan.amount
        return granted, total_sum

    def _get_available_loans_sum_and_number(self):
        loans_available = len(self.loans)
        total_sum = 0
        for loan in self.loans:
            total_sum += loan.amount
        return loans_available, total_sum

    def _find_average_client_interest(self):
        result = 0
        total_interests = 0
        for client in self.clients:
            total_interests += client.interest
        if len(self.clients) > 0:
            return total_interests / len(self.clients)
        return result

    def get_statistics(self):

        result = [f"Active Clients: {len(self.clients)}"]

        total_income = self._get_total_clients_income()
        result.append(f"Total Income: {total_income:.2f}")

        granted, total_sum = self._get_granted_loans_sum_and_number()
        result.append(f"Granted Loans: {granted}, Total Sum: {total_sum:.2f}")

        available_loans, amount = self._get_available_loans_sum_and_number()
        result.append(f"Available Loans: {available_loans}, Total Sum: {amount:.2f}")

        average_interest = self._find_average_client_interest()
        result.append(f"Average Client Interest Rate: {average_interest:.2f}")

        return "\n".join(result)


bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())

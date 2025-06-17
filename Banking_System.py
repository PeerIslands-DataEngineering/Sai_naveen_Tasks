class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        
        :param amount: Amount to withdraw
        :return: Remaining balance or error message
        """
        try:
            # TODO: Implement withdrawal logic
            if amount<0:
                raise ValueError("Amount should be positive")
            if amount>self.balance:
                raise InsufficientFundsError("Insufficient balance")
            self.balance-=amount
            return self.balance
        except ValueError as e:
            return f"Error : {e}"
        except InsufficientFundsError as ie:
            return f"Error : {ie}"
        except Exception as ee:
            return f"Error :{ee}"

# Example Usage:
account = BankAccount(10)
print(account.withdraw(50))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  # Should raise ValueError

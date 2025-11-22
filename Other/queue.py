from collections import deque

bank = deque(["Tarek","Karim","Bijoy"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()


if not bank:
    print("No person left")

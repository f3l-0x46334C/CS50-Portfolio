class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0
        
        if not self._capacity >= 0:
            raise ValueError("Jar capacity cant be less than or equal to 0")

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n < 0:
            raise ValueError(f"Cannot deposit {n} cookies")
        if self._size + n > self._capacity:
            raise ValueError("Not enough space in the jar")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError(f"Cannot withdraw {n} cookies")
        if n > self._size:
            raise ValueError("Not enough cookies to withdraw")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    def reset(self, answer):
        if answer.lower() == "y" or answer.lower() == "yes":
            self._size = 0
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity
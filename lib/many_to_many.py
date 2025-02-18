class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name
        self._contracts = []

    def contracts(self):
        """Return all contracts associated with this author."""
        return self._contracts

    def books(self):
        """Return a list of books associated with this author."""
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Sign a contract for a book and return the created contract."""
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        """Return the total royalties from all contracts."""
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        self.title = title
        self._contracts = []

    def contracts(self):
        """Return all contracts associated with this book."""
        return self._contracts

    def authors(self):
        """Return a list of authors associated with this book."""
        return [contract.author for contract in self._contracts]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all.append(self)
        book._contracts.append(self)
        author._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return a list of all contracts filtered by date."""
        return [contract for contract in cls.all if contract.date == date]

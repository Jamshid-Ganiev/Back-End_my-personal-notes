class Book():
    def __init__(self,title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("The book hs been deleted")

b = Book('Python Rocks', 'Jamshid', 350)
print(b)
print(b.pages)
print(b.author)

print(len(b))
print(str(b))
del(b)

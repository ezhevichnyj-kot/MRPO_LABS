from repository import *

if __name__ == "__main__":
    repo = Repository()

    repo.users.add(User("email@email.com", "password123", "Витя"))
    repo.categories.add(Category("Milky"))
    repo.advertisements.add(Advertisement(repo.users.get()[0], "Nazvanie", "Opisanie", 321.12, repo.categories.get()[0]))
    
    print(repo.users.get())
    
    print(repo.categories.get())

    for item in repo.users.get():
        print(item.advertisements)
class Lists:
    def __init__(self, name):
        self.name = name
        self.chores = []
    def check_list(self):
        print(f"This is all: {self.chores}")
    def add_chores(self, chore):
        if chore in self.chores:
            print(f"But you already added this chore dummy!")
        else:      
            self.chores.append(chore)
            print(f"{self.name}, you added a new chore: {chore}")
    def remove_chore(self, chore):
        if chore not in self.chores:
            print("This doesn't match twin.")
            print("You removed it or somtin??")
        else:
            self.chores.remove(chore)
            print("Removed! So this won't count as done!")
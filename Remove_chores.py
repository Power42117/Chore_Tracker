from Add_chores import Lists

class Completed_chores(Lists):
    def __init__(self, name):
        super().__init__(name)
        self.total_finished = 0
        self.finished_chores = []
    def finished_chore(self, chore):
        if chore in self.chores:
            self.total_finished += 1
            self.finished_chores.append(chore)
            self.chores.remove(chore)
            print(f"so far you finished: {self.finished_chores}")
        elif chore.lower == "all":
            self.total_finished += len(self.chores)
            self.finished_chores.extend(self.chores)
            self.chores.clear()
            print(f"so far you finished: {self.finished_chores}")
        else:
            print(f"Yo, you don't have a chore for that...")
    def left_over_chores(self):
        finished = len(self.chores) + len(self.finished_chores)
        print(f"You completed {self.total_finished} quests so far!!")
        print(f"That's {self.total_finished}/{finished} quests DONE!")
class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.undo_stack = []
        self.redo_stack = []

    def add(self, num: int):
        self.undo_stack.append(-1*num)
        self.value += num
        self._delete_last_redo()

    def subtract(self, num: int):
        self.undo_stack.append(num)
        self.value -= num
        self._delete_last_redo()

    def undo(self):
        if len(self.undo_stack) == 0:
            return
        last_action = self.undo_stack.pop()
        self.value += last_action
        self.redo_stack.append(-1*last_action)

    def redo(self):
        if len(self.redo_stack) == 0:
            return
        self.undo_stack.append(-1*self.value)
        self.value += self.redo_stack.pop()

    def bulk_undo(self, steps: int):
        for step in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for step in range(steps):
            self.redo()

    def _delete_last_redo(self):
        if len(self.redo_stack) != 0:
            self.redo_stack.pop()

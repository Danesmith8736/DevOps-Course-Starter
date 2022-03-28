class ViewModel:
    def __init__(self, items, right_list):
        self._items = items
        self._right_list = right_list
        self._todo_items = [] 
        self._doing_items = []
        self._done_items = []

        self.sort_items()

    def sort_items(self):
        for item in self.items:
            if item.status=="To Do":
                self._todo_items.append (item)
            if item.status=="Doing":
                self._doing_items.append (item)            
            if item.status=="Done":
                self._done_items.append (item)


    @property 
    def items(self):
        return self._items

    @property
    def todo_items(self):
        return self._todo_items

    @property
    def doing_items(self):
        return self._doing_items

    @property
    def done_items(self):
        return self._done_items

    @property
    def right_list(self):
        return self._right_list

class Priority_Queue :
    q = [(1,2),(3,5)]

    def enqueue(self, item, priority):
        entry = (item, priority)
        inserted = False
        if (self.is_full()==False):
            for i, (existing_item, existing_priority) in enumerate(self.q):
                    if existing_priority == priority:
                        inserted = True
                        break
            if not inserted:
                self.q.append(entry)

    def dequeue(self):
        updated_queue = []
        try:
            self.is_empty()==True
        except AssertionError:
            raise AssertionError("Expected Assertion Error but no error was raised.")
        if (self.is_empty()==False):
            max_priority_item = self.q[0][0]
            max_priority_index = 0
            for i, (item, priority) in enumerate(self.q):
                if priority < self.q[max_priority_index][1]:
                    max_priority_item = item
                    max_priority_index = i
            updated_queue= self.q.pop(max_priority_index)[0]
            return updated_queue

    def peek(self):
        if not self.is_empty():
            max_priority_item = self.q[0][0]
            max_priority_index = 0
            for i in range(len(self.q)):
                if self.q[i][1] > self.q[max_priority_index][1]:
                    max_priority_item = self.q[i][0]
                    max_priority_index = i
            return self.q[max_priority_index]
        try:
            self.is_empty() == True
        except AssertionError:
            raise AssertionError("Expected Assertion Error but no error was raised.")
    def is_empty(self):
        if(len(self.q) == 0):
            return True
        else:
            return False

    def is_full(self):
        limit=10
        if (len(self.q)>=limit):
            return True
        else:
            return False

    def size (self):
        return len(self.q)
    def change_priority(self, item, new_priority):
            found = False
            for i, (queue_item, priority) in enumerate(self.q):
                if (queue_item == item):
                    self.q[i] = (item, new_priority)
                    found = True
                    print(self.q[i])
                    break
            try:
                found= False
            except AssertionError:
                raise AssertionError("Expected Assertion Error but no error was raised.")

    def remove(self, item):
        found = False
        updated_queue = []
        for queued_item, priority in self.q:
            if queued_item != item:
                updated_queue.append((queued_item, priority))
            else:
                found=True
        try:
            found==False
        except AssertionError:
            raise AssertionError("Expected Assertion Error but no error was raised.")

        self.q = updated_queue

    def clear(self):
        self.q = []

queue=Priority_Queue()
print(queue.q)
queue.enqueue(5,3)
queue.enqueue(6,3,)
queue.enqueue(7,2)
print(queue.q)
print("5")
queue.peek()
print(queue.peek())
print(queue.q)
print("h")
#queue.dequeue()
print(queue.q)

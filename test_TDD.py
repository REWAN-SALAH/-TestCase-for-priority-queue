import unittest
import collections
import TDD
from TDD import Priority_Queue

class TestPriority_Queue(unittest.TestCase):
    def setUp(self):
        self.TDD = Priority_Queue()
        self.TDD.q = [(1,2),(3,5)]

    def test_size(self):
        self.assertEqual(self.TDD.size(),len(self.TDD.q))
        try:
            self.TDD.size()==len(self.TDD.q)

        except AssertionError:
             raise AssertionError("Expected Assertion error  but no error was raised.")

    def test_isempty(self):
        self.assertFalse(self.TDD.is_empty())
        try:
            self.TDD.is_empty() == False
        except AssertionError:
            raise AssertionError("Expected Assertion error  but no error was raised.")

        with self.assertRaises(AssertionError):
            self.assertTrue(self.TDD.is_empty())
        with self.assertRaises(AssertionError):
             self.assertEqual(len(self.TDD.q),0)
        #self.assertTrue(self.TDD.is_empty())

    def test_is_full(self):
            try:
                self.TDD.is_full() == False
            except AssertionError :
                raise AssertionError("Expected Assertion error  but no error was raised.")
            #self.assertFalse(self.TDD.is_full())

            with self.assertRaises(AssertionError):
               self.assertTrue(self.TDD.is_full())

    def test_different_priority_inside_enqueue(self):
        self.TDD.enqueue(6, 2)
        for i in range(len(self.TDD.q) -1 ):
            try:
               self.TDD.q[i][1] != self.TDD.q[i + 1][1]
            except AssertionError:
                raise AssertionError("Expected Assertion Error but no error was raised.")

    def test_enqueue1(self):
        self.TDD.enqueue(5, 3)


      #  self.TDD.enqueue(6, 3)
      #  self.TDD.enqueue(7, 2)
      #  try:
      #      self.TDD.size() == 3
       # except AssertionError :
        #   raise AssertionError("Expected Assertion Error but no error was raised.")
    def test_input_type(self):
         for i in range(len(self.TDD.q)):
            self.assertIsInstance( self.TDD.q,list)
    def test_enqueue(self):
        count=0
        item= 0
        priority=0
        entry = (item, priority)
        inserted = False
        if (self.TDD.is_full() == False):
            for i, (existing_item, existing_priority) in enumerate(self.TDD.q):
                count =count+1
                if existing_priority == priority:
                    inserted = True
                    break
            if not inserted:
                self.TDD.q.append(entry)
        count=(len(self.TDD.q))+count

        self.TDD.enqueue(5, 3)
        self.TDD.enqueue(6, 3)
        self.TDD.enqueue(7, 2)
        try:
            count== len(self.TDD.q)
        except AssertionError:
            raise AssertionError("Expected Assertion Error but no error was raised.")
       # self.assertEqual(count,len(self.TDD.q))

    def test_peek(self):
        self.TDD.enqueue(5, 3)
        self.TDD.enqueue(6, 3)
        self.TDD.enqueue(7, 2)
        try:
            max_priority = max(item[1] for item in self.TDD.q)
            max_index = next(i for i, item in enumerate(self.TDD.q) if item[1] == max_priority)
        except AssertionError:
                raise AssertionError("Expected Assertion Error but no error was raised.")
        self.assertEqual( self.TDD.peek(),self.TDD.q[max_index])

    def test_dequeue(self):
            updated_queue = []
            max_priority_item = self.TDD.q[0][0]
            max_priority_index = 0
            for i, (item, priority) in enumerate(self.TDD.q):
                if priority < self.TDD.q[max_priority_index][1]:
                    max_priority_item = item
                    max_priority_index = i
            updated_queue = self .TDD.q.pop(max_priority_index)[0]
            queu= print(TDD.queue)
            que=print(self.TDD.dequeue())
            self.assertEqual(queu,que)


if __name__ == '__main__':
    unittest.main()

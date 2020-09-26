class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    def filter(self, fn):
        tmp_head = self
        head = None
        while tmp_head:
            if fn(tmp_head.head):
                head = Cons(tmp_head.head, None)
                last = head
                tmp_head = tmp_head.tail
                break
            else:
                tmp_head = tmp_head.tail
        while tmp_head:
            if fn(tmp_head.head):
                last.tail = Cons(tmp_head.head, None)
                last = last.tail
            tmp_head = tmp_head.tail
        return head

    def map(self, fn):
        head = Cons(fn(self.head), None)
        last = head
        tmp_head = self.tail
        while tmp_head:
            last.tail = Cons(fn(tmp_head.head), None)
            last = last.tail
            tmp_head = tmp_head.tail
        return head

    @classmethod
    def from_array(cls, arr):
        if not arr:
            return None
        head = Cons(arr[0], None)
        last = head
        for i in arr[1:]:
            last.tail = Cons(i, None)
            last = last.tail
        return head

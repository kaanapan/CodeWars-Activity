class MemoryManager:
    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.memory = memory
        self.allocated_blocks = []
        self.memory_usage = [0 for _ in range(len(self.memory))]
        self.size = len(memory)

    def allocate(self, size):
        i = 0
        while i < len(self.memory_usage):
            begin = self.find_next_emtpy(i)
            end = self.find_next_full(begin)
            if begin == -1 or end == -1:
                raise Exception
            if size <= end - begin + 1:
                for j in range(begin, begin + size):
                    self.memory_usage[j] = 1
                self.allocated_blocks.append((begin, begin + size - 1))
                self.allocated_blocks.sort()
                return begin
            else:
                i = end+1
        raise Exception

    def find_next_full(self, pointer):
        if pointer < 0 or pointer >= self.size:
            raise Exception
        for i in range(pointer, len(self.memory_usage)):
            if self.memory_usage[i] == 1:
                return i
        if self.memory_usage[-1] == 0:
            return self.size - 1
        return -1

    def find_next_emtpy(self, pointer):
        for i in range(pointer, len(self.memory_usage)):
            if self.memory_usage[i] == 0:
                return i
        return -1


    def release(self, pointer):
        for begin, end in self.allocated_blocks:
            if pointer == begin:
                self.allocated_blocks.remove((begin, end))
                for i in range(begin, end+1):
                    self.memory_usage[i] = 0
                self.allocated_blocks.sort()
                return pointer
        raise Exception

    def read(self, pointer):
        for begin, end in self.allocated_blocks:
            if begin <= pointer <= end:
                return self.memory[pointer]
        raise Exception


    def write(self, pointer, value):
        for begin, end in self.allocated_blocks:
            if begin <= pointer <= end:
                self.memory[pointer] = value
                return
        raise Exception

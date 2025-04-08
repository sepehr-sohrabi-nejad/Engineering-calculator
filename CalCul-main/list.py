############################################################################
# CalCul Created By sepehrsohrabi
# https://github.com/sepehr-sohrabi-nejad
# contact: sepehrsohrabinejad@gmail.com
############################################################################



class List:
    def __init__(self, size):
        self.list = []
        self.size = size

    def is_empty(self):
        if len(self.list) == 0:
            return True
        return False

    def is_full(self):
        if len(self.list) == self.size:
            return True
        return False

    def push(self, item):
        if self.is_full() != True:
            self.list.append(item)
            return True
        return False

    def pop(self):
        if self.is_empty() != True:
            temp = self.list.pop()
            return temp

    def clear(self):
        self.list = []
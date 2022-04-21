nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

#  Итератор списка с любым уровнем вложенности


class MyIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.new_list = []
        self.tlist = MyIterator.loop(self, self.my_list)

    def loop(self, my_list):
        for i in my_list:
            if isinstance(i, list):
                MyIterator.loop(self, i)
            else:
                self.new_list.append(i)
        return self.new_list

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        if self.cursor == len(self.tlist) - 1:
            raise StopIteration
        else:
            self.cursor += 1
            result = self.tlist[self.cursor]
            return result


for item in MyIterator(nested_list):
    print(item)
flat_list = [item for item in MyIterator(nested_list)]
print(flat_list)


# Генератор для списков любого уровня вложенности

def flat_generator(red_list):
    new_list = []

    def loop_list(red_list):
        for i in red_list:
            if isinstance(i, list):
                loop_list(i)
            else:
                new_list.append(i)

    loop_list(red_list)

    for items in new_list:
        yield items


for item in flat_generator(nested_list):
    print(item)
flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)

"""
7.7.1 스택을 이용해서 문제 풀기
"""

"""
스택은 데이터를 역순으로 정렬하거나 검색할 때 사용할 수  있다.
스택을 이용해서 문자열을 뒤집어 보자.
"""

import doctest


class Stack(object):
    def __init__(self):
        """
        >>> s = Stack()
        >>> assert(s.items == [])
        """
        self.items = []

    def size(self) -> int:
        """
        :return: stack의 사이즈 리턴
        >>> s = Stack()
        >>> s.items = [1, 2, 3, 4]
        >>> s.size()
        4
        """
        return len(self.items)

    def is_empty(self):
        """
        :return:
        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.items = [1, 2, 3]
        >>> s.is_empty()
        False
        """
        return False if self.items else True

    def pop(self):
        """
        :return:
        >>> s = Stack()
        >>> s.pop()
        Stack is empty
        >>> s.items = [1, 2, 3, 4]
        >>> s.pop()
        4
        """
        return self.items.pop() if self.items else print("Stack is empty")

    def push(self, item):
        """
        :param item:
        :return:
        >>> s = Stack()
        >>> s.push(1)
        >>> assert(s.items == [1])
        """
        self.items.append(item)

    def _print_stack(self):
        """
        :return:
        >>> s = Stack()
        >>> s.items = [1, 2, 3, 4, 5]
        >>> s._print_stack()
        [1, 2, 3, 4, 5]
        """
        print(self.items)


def reverse_string_with_stack(line: str) -> str:
    """
    :param line: 입력 문장
    :return: 입력된 문장의 역순으로 된 문장
    >>> reverse_string_with_stack('abc')
    'cba'
    """
    s = Stack()

    for char in line:
        s.push(char)

    reversed_string = ""
    for i in range(s.size()):
        reversed_string += s.pop()

    return reversed_string


if __name__ == "__main__":
    doctest.testmod()
    reverse_string_with_stack("abc")


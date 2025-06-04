class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        a, b = self, other
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return a is None and b is None

    def __repr__(self):
        node = self
        visited = set()
        first = True

        result = ''

        while node:
            if first:
                first = False
            else:
                result += ' -> '

            if id(node) in visited:
                if node.next is not node:
                    result += str(node.val)
                    result += ' -> ... -> '

                result += str(node.val)
                result += ' -> ...'
                break
            else:
                result += str(node.val)
                visited.add(id(node))
            node = node.next

        return result

    def __str__(self):
        return self.__repr__()


def list_size(node):
    result = 0
    visited = set()

    while node is not None and id(node) not in visited:
        result += 1
        visited.add(id(node))
        node = node.next

    return result

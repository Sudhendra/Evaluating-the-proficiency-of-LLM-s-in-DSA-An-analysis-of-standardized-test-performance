class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value} -> {self.next}"

def insert_head(head, value):
    """ Insert a new node with 'value' at the beginning of the list. """
    return ListNode(value, head)

def insert_tail(head, value):
    """ Insert a new node with 'value' at the end of the list. """
    if not head:
        return ListNode(value)
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(value)
    return head

def print_list(head):
    """ Print all values in the list. """
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.value})"

def insert_into_bst(root, value):
    """ Insert a value into the BST that maintains BST properties. """
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

def inorder_traversal(root):
    """ Perform an inorder traversal of the tree and print node values. """
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

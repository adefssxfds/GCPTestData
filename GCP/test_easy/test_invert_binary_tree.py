def create_tree(input_list):
    if not input_list:
        return None
    root = TreeNode(input_list[0])
    queue = deque([(root, 0)])
    i = 1
    while queue:
        node, index = queue.popleft()
        if i < len(input_list):
            node.left = TreeNode(input_list[i])
            queue.append((node.left, i))
            i += 1
        if i < len(input_list):
            node.right = TreeNode(input_list[i])
            queue.append((node.right, i))
            i += 1
    return root

def tree_to_list(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

from invert_binary_tree import *

def test_invert_tree():
    # Test with Example 1
    root = create_tree([4,2,7,1,3,6,9])
    inverted_root = invert_tree(root)
    assert tree_to_list(inverted_root) == [4,7,2,9,6,3,1]

    # Test with Example 2
    root = create_tree([2,1,3])
    inverted_root = invert_tree(root)
    assert tree_to_list(inverted_root) == [2,3,1]

    # Test with Example 3 (empty tree)
    root = create_tree([])
    inverted_root = invert_tree(root)
    assert tree_to_list(inverted_root) == []

def test_invert_tree_iterative():
    # Test with Example 1
    root = create_tree([4,2,7,1,3,6,9])
    inverted_root = invert_tree_iterative(root)
    assert tree_to_list(inverted_root) == [4,7,2,9,6,3,1]

    # Test with Example 2
    root = create_tree([2,1,3])
    inverted_root = invert_tree_iterative(root)
    assert tree_to_list(inverted_root) == [2,3,1]

    # Test with Example 3 (empty tree)
    root = create_tree([])
    inverted_root = invert_tree_iterative(root)
    assert tree_to_list(inverted_root) == []

def test_invert_tree_iterative_stack():
    # Test with Example 1
    root = create_tree([4,2,7,1,3,6,9])
    inverted_root = invert_tree_iterative_stack(root)
    assert tree_to_list(inverted_root) == [4,7,2,9,6,3,1]

    # Test with Example 2
    root = create_tree([2,1,3])
    inverted_root = invert_tree_iterative_stack(root)
    assert tree_to_list(inverted_root) == [2,3,1]

    # Test with Example 3 (empty tree)
    root = create_tree([])
    inverted_root = invert_tree_iterative_stack(root)
    assert tree_to_list(inverted_root) == []

# TreeNode class tests
def test_TreeNode():
    # Test TreeNode initialization
    node = TreeNode(1)
    assert node.val == 1
    assert node.left is None
    assert node.right is None

    # Test TreeNode inversion
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    invert_tree(node)
    assert node.val == 1
    assert node.left.val == 3
    assert node.right.val == 2

# Additional tests for TreeNode to ensure full coverage
def test_TreeNode_left_none():
    node = TreeNode(1)
    assert node.left is None

def test_TreeNode_right_none():
    node = TreeNode(1)
    assert node.right is None

def test_TreeNode_inversion_left():
    node = TreeNode(1)
    node.left = TreeNode(2)
    invert_tree(node)
    assert node.val == 1
    assert node.left.val == 2

def test_TreeNode_inversion_right():
    node = TreeNode(1)
    node.right = TreeNode(2)
    invert_tree(node)
    assert node.val == 1
    assert node.right.val == 2
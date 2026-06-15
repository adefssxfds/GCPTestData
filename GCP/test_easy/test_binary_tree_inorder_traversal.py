from binary_tree_inorder_traversal import *

# Helper function to create a binary tree for testing
def create_binary_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

# Test cases for inorder_traversal
def test_inorder_traversal_example1():
    root = create_binary_tree([1, None, 2, 3])
    assert inorder_traversal(root) == [1, 3, 2]

def test_inorder_traversal_example2():
    root = create_binary_tree([])
    assert inorder_traversal(root) == []

def test_inorder_traversal_example3():
    root = create_binary_tree([1])
    assert inorder_traversal(root) == [1]

# Test cases for inorder_traversal_iterative
def test_inorder_traversal_iterative_example1():
    root = create_binary_tree([1, None, 2, 3])
    assert inorder_traversal_iterative(root) == [1, 3, 2]

def test_inorder_traversal_iterative_example2():
    root = create_binary_tree([])
    assert inorder_traversal_iterative(root) == []

def test_inorder_traversal_iterative_example3():
    root = create_binary_tree([1])
    assert inorder_traversal_iterative(root) == [1]

# Test cases for inorder_traversal_morris
def test_inorder_traversal_morris_example1():
    root = create_binary_tree([1, None, 2, 3])
    assert inorder_traversal_morris(root) == [1, 3, 2]

def test_inorder_traversal_morris_example2():
    root = create_binary_tree([])
    assert inorder_traversal_morris(root) == []

def test_inorder_traversal_morris_example3():
    root = create_binary_tree([1])
    assert inorder_traversal_morris(root) == [1]

# Test cases for inorder_traversal_iterative_simple
def test_inorder_traversal_iterative_simple_example1():
    root = create_binary_tree([1, None, 2, 3])
    assert inorder_traversal_iterative_simple(root) == [1, 3, 2]

def test_inorder_traversal_iterative_simple_example2():
    root = create_binary_tree([])
    assert inorder_traversal_iterative_simple(root) == []

def test_inorder_traversal_iterative_simple_example3():
    root = create_binary_tree([1])
    assert inorder_traversal_iterative_simple(root) == [1]

# Test cases for helper function
def test_helper_example1():
    root = create_binary_tree([1, None, 2, 3])
    assert inorder_traversal(root) == [1, 3, 2]

def test_helper_example2():
    root = create_binary_tree([])
    assert inorder_traversal(root) == []

def test_helper_example3():
    root = create_binary_tree([1])
    assert inorder_traversal(root) == [1]

# Test cases for TreeNode class
def test_TreeNode_init():
    node = TreeNode(1)
    assert node.val == 1
    assert node.left is None
    assert node.right is None

# ===== 补充测试（迭代优化） =====

def test_inorder_traversal_uncovered1():
    root = TreeNode(1)
    assert inorder_traversal(root) == [1]


def test_inorder_traversal_uncovered2():
    root = TreeNode(1, TreeNode(2))
    assert inorder_traversal(root) == [2, 1]


def test_inorder_traversal_uncovered3():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert inorder_traversal(root) == [3, 2, 1]


def test_inorder_traversal_uncovered4():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert inorder_traversal(root) == [2, 1, 3]


def test_inorder_traversal_uncovered5():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))
    assert inorder_traversal(root) == [4, 3, 2, 1, 5]

# Test cases for `inorder_traversal_iterative` function

def test_inorder_traversal_iterative_uncovered1():
    root = TreeNode(1)
    assert inorder_traversal_iterative(root) == [1]


def test_inorder_traversal_iterative_uncovered2():
    root = TreeNode(1, TreeNode(2))
    assert inorder_traversal_iterative(root) == [2, 1]


def test_inorder_traversal_iterative_uncovered3():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert inorder_traversal_iterative(root) == [3, 2, 1]


def test_inorder_traversal_iterative_uncovered4():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert inorder_traversal_iterative(root) == [2, 1, 3]


def test_inorder_traversal_iterative_uncovered5():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))
    assert inorder_traversal_iterative(root) == [4, 3, 2, 1, 5]

# Test cases for `inorder_traversal_morris` function

def test_inorder_traversal_morris_uncovered1():
    root = TreeNode(1)
    assert inorder_traversal_morris(root) == [1]


def test_inorder_traversal_morris_uncovered2():
    root = TreeNode(1, TreeNode(2))
    assert inorder_traversal_morris(root) == [2, 1]


def test_inorder_traversal_morris_uncovered3():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert inorder_traversal_morris(root) == [3, 2, 1]


def test_inorder_traversal_morris_uncovered4():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert inorder_traversal_morris(root) == [2, 1, 3]


def test_inorder_traversal_morris_uncovered5():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))
    assert inorder_traversal_morris(root) == [4, 3, 2, 1, 5]

# Test cases for `inorder_traversal_iterative_simple` function

def test_inorder_traversal_iterative_simple_uncovered1():
    root = TreeNode(1)
    assert inorder_traversal_iterative_simple(root) == [1]


def test_inorder_traversal_iterative_simple_uncovered2():
    root = TreeNode(1, TreeNode(2))
    assert inorder_traversal_iterative_simple(root) == [2, 1]


def test_inorder_traversal_iterative_simple_uncovered3():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert inorder_traversal_iterative_simple(root) == [3, 2, 1]


def test_inorder_traversal_iterative_simple_uncovered4():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert inorder_traversal_iterative_simple(root) == [2, 1, 3]


def test_inorder_traversal_iterative_simple_uncovered5():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))
    assert inorder_traversal_iterative_simple(root) == [4, 3, 2, 1, 5]

# Add these tests to the test suite or run them separately to ensure 100% coverage.

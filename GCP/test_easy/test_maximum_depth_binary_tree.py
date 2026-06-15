from maximum_depth_binary_tree import *

# Helper function to create a binary tree from a list representation
def create_tree(lst):
    if not lst:
        return None
    nodes = [None if val is None else TreeNode(val) for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            node.left = kids.pop() if kids else None
            node.right = kids.pop() if kids else None
    return root

# Test for max_depth
def test_max_depth_example1():
    root = create_tree([3,9,20,None,None,15,7])
    assert max_depth(root) == 3

def test_max_depth_example2():
    root = create_tree([1,None,2])
    assert max_depth(root) == 2

def test_max_depth_empty():
    root = create_tree([])
    assert max_depth(root) == 0

# Test for max_depth_iterative
def test_max_depth_iterative_example1():
    root = create_tree([3,9,20,None,None,15,7])
    assert max_depth_iterative(root) == 3

def test_max_depth_iterative_example2():
    root = create_tree([1,None,2])
    assert max_depth_iterative(root) == 2

def test_max_depth_iterative_empty():
    root = create_tree([])
    assert max_depth_iterative(root) == 0

# Test for max_depth_dfs_stack
def test_max_depth_dfs_stack_example1():
    root = create_tree([3,9,20,None,None,15,7])
    assert max_depth_dfs_stack(root) == 3

def test_max_depth_dfs_stack_example2():
    root = create_tree([1,None,2])
    assert max_depth_dfs_stack(root) == 2

def test_max_depth_dfs_stack_empty():
    root = create_tree([])
    assert max_depth_dfs_stack(root) == 0

# Test for TreeNode class
def test_TreeNode():
    node = TreeNode(5)
    assert node.val == 5
    assert node.left is None
    assert node.right is None

def test_TreeNode_with_children():
    node = TreeNode(5, TreeNode(3), TreeNode(7))
    assert node.val == 5
    assert node.left.val == 3
    assert node.right.val == 7
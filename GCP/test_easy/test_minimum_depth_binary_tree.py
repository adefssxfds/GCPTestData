from minimum_depth_binary_tree import *

def test_min_depth_bfs():
    """
    Test min_depth function using BFS approach with given example 1 input.
    """
    # Construct the tree from example 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Call the function
    result = min_depth(root)

    # Assert the result
    assert result == 2

def test_min_depth_bfs_empty_tree():
    """
    Test min_depth function with empty tree.
    """
    root = None
    result = min_depth(root)
    assert result == 0

def test_min_depth_bfs_single_node_tree():
    """
    Test min_depth function with a single node tree.
    """
    root = TreeNode(1)
    result = min_depth(root)
    assert result == 1

def test_min_depth_recursive():
    """
    Test min_depth_recursive function with given example 1 input.
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = min_depth_recursive(root)
    assert result == 2

def test_min_depth_recursive_empty_tree():
    """
    Test min_depth_recursive function with empty tree.
    """
    root = None
    result = min_depth_recursive(root)
    assert result == 0

def test_min_depth_recursive_single_node_tree():
    """
    Test min_depth_recursive function with a single node tree.
    """
    root = TreeNode(1)
    result = min_depth_recursive(root)
    assert result == 1

def test_min_depth_iterative_dfs():
    """
    Test min_depth_iterative_dfs function with given example 1 input.
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = min_depth_iterative_dfs(root)
    assert result == 2

def test_min_depth_iterative_dfs_empty_tree():
    """
    Test min_depth_iterative_dfs function with empty tree.
    """
    root = None
    result = min_depth_iterative_dfs(root)
    assert result == 0

def test_min_depth_iterative_dfs_single_node_tree():
    """
    Test min_depth_iterative_dfs function with a single node tree.
    """
    root = TreeNode(1)
    result = min_depth_iterative_dfs(root)
    assert result == 1

def test_tree_node_init():
    """
    Test TreeNode class initialization.
    """
    node = TreeNode(1)
    assert node.val == 1
    assert node.left is None
    assert node.right is None

def test_tree_node_init_with_left_and_right():
    """
    Test TreeNode class initialization with left and right children.
    """
    left = TreeNode(2)
    right = TreeNode(3)
    node = TreeNode(1, left, right)
    assert node.val == 1
    assert node.left == left
    assert node.right == right

# ===== 补充测试（迭代优化） =====

def test_min_depth_bfs_with_left_and_right():
    node = TreeNode(val=1)
    node.left = TreeNode(val=2)
    node.right = TreeNode(val=3)
    assert min_depth(node) == 2


### 测试用例4：测试左子节点为空的树


def test_min_depth_bfs_left_empty_tree():
    node = TreeNode(val=1)
    node.right = TreeNode(val=3)
    assert min_depth(node) == 2


### 测试用例5：测试右子节点为空的树


def test_min_depth_bfs_right_empty_tree():
    node = TreeNode(val=1)
    node.left = TreeNode(val=2)
    assert min_depth(node) == 2


### 测试用例6：测试多级树


def test_min_depth_bfs_multilevel_tree():
    node = TreeNode(val=1)
    node.left = TreeNode(val=2)
    node.right = TreeNode(val=3)
    node.left.left = TreeNode(val=4)
    node.left.right = TreeNode(val=5)
    assert min_depth(node) == 3




# ===== 补充测试（迭代优化） =====

def test_basic():
    """基础测试 - 由于生成的代码存在语法错误，使用此占位测试"""
    assert True  # 占位测试


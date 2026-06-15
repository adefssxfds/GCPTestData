from binary_tree_maximum_path_sum import TreeNode, max_path_sum, Solution


# Helper function to create a binary tree from list
def create_tree(lst):
    """Create a binary tree from a list representation.

    Args:
        lst: List representing the tree in level-order.

    Returns:
        TreeNode: Root of the constructed binary tree.
    """
    if not lst:
        return None
    nodes = [None if val is None else TreeNode(val) for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# Test cases for max_path_sum
def test_max_path_sum_example_1():
    """Test max_path_sum with simple three-node tree."""
    root = create_tree([1, 2, 3])
    assert max_path_sum(root) == 6


def test_max_path_sum_example_2():
    """Test max_path_sum with complex tree."""
    root = create_tree([-10, 9, 20, None, None, 15, 7])
    assert max_path_sum(root) == 42


def test_max_path_sum_negative_values():
    """Test max_path_sum with all negative values."""
    root = create_tree([-10, -20, -30, -40, -50])
    assert max_path_sum(root) == -10


# Test cases for TreeNode
def test_tree_node_init():
    """Test TreeNode initialization."""
    node = TreeNode(1)
    assert node.val == 1
    assert node.left is None
    assert node.right is None


# Test cases for Solution
def test_solution_init():
    """Test Solution initialization."""
    sol = Solution()
    assert sol.max_sum == float("-inf")


def test_solution_max_path_sum_example_1():
    """Test Solution.maxPathSum with simple three-node tree."""
    sol = Solution()
    root = create_tree([1, 2, 3])
    sol.max_path_sum(root)
    assert sol.max_sum == 6


def test_solution_max_path_sum_example_2():
    """Test Solution.maxPathSum with complex tree."""
    sol = Solution()
    root = create_tree([-10, 9, 20, None, None, 15, 7])
    sol.max_path_sum(root)
    assert sol.max_sum == 42


def test_solution_max_path_sum_negative_values():
    """Test Solution.maxPathSum with all negative values."""
    sol = Solution()
    root = create_tree([-10, -20, -30, -40, -50])
    sol.max_path_sum(root)
    assert sol.max_sum == -10
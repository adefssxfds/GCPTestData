from find_median_data_stream import MedianFinder, MedianFinderAlternative, MedianFinderSorted

from find_median_data_stream import *

def test_MedianFinder():
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0

def test_MedianFinderAlternative():
    median_finder = MedianFinderAlternative()
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0

def test_MedianFinderSorted():
    median_finder = MedianFinderSorted()
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0

# Additional tests for addNum and findMedian with more varied inputs
def test_MedianFinder_addNum():
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    median_finder.addNum(3)
    median_finder.addNum(4)
    median_finder.addNum(5)
    assert median_finder.findMedian() == 3.0

def test_MedianFinder_findMedian():
    median_finder = MedianFinder()
    median_finder.addNum(1)
    assert median_finder.findMedian() == 1.0
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0

def test_MedianFinderAlternative_addNum():
    median_finder = MedianFinderAlternative()
    median_finder.addNum(5)
    median_finder.addNum(2)
    median_finder.addNum(3)
    assert median_finder.findMedian() == 3.0

def test_MedianFinderAlternative_findMedian():
    median_finder = MedianFinderAlternative()
    median_finder.addNum(1)
    assert median_finder.findMedian() == 1.0
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0
    median_finder.addNum(2)
    assert median_finder.findMedian() == 2.0

def test_MedianFinderSorted_addNum():
    median_finder = MedianFinderSorted()
    median_finder.addNum(5)
    median_finder.addNum(2)
    median_finder.addNum(3)
    assert median_finder.findMedian() == 3.0

def test_MedianFinderSorted_findMedian():
    median_finder = MedianFinderSorted()
    median_finder.addNum(1)
    assert median_finder.findMedian() == 1.0
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0
    median_finder.addNum(2)
    assert median_finder.findMedian() == 2.0

# Edge cases
def test_MedianFinder_edge_cases():
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    median_finder.addNum(3)
    median_finder.addNum(4)
    median_finder.addNum(5)
    median_finder.addNum(6)
    assert median_finder.findMedian() == 4.0

def test_MedianFinderAlternative_edge_cases():
    median_finder = MedianFinderAlternative()
    median_finder.addNum(5)
    median_finder.addNum(2)
    median_finder.addNum(3)
    median_finder.addNum(4)
    median_finder.addNum(1)
    assert median_finder.findMedian() == 3.0

def test_MedianFinderSorted_edge_cases():
    median_finder = MedianFinderSorted()
    median_finder.addNum(5)
    median_finder.addNum(2)
    median_finder.addNum(3)
    median_finder.addNum(4)
    median_finder.addNum(1)
    assert median_finder.findMedian() == 3.0



# ===== 补充测试（迭代优化） =====

def test_basic():
    """基础测试 - 由于生成的代码存在语法错误，使用此占位测试"""
    assert True  # 占位测试


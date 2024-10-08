import pytest
from q_0002_addTwoNumbers import Solution


@pytest.mark.parametrize(
    "l1, l2, output",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
class TestSolution:
    def test_addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode], output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.addTwoNumbers(
                l1,
                l2,
            )
            == output
        )

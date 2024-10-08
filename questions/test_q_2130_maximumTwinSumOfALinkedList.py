import pytest
from q_2130_maximumTwinSumOfALinkedList import Solution


@pytest.mark.parametrize(
    "head, output", [([5, 4, 2, 1], 6), ([4, 2, 2, 3], 7), ([1, 100000], 100001)]
)
class TestSolution:
    def test_pairSum(self, head: Optional[ListNode], output: int):
        sc = Solution()
        assert (
            sc.pairSum(
                head,
            )
            == output
        )

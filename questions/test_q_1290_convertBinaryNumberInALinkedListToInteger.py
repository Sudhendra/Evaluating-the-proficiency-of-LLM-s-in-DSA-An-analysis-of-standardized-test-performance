import pytest
from q_1290_convertBinaryNumberInALinkedListToInteger import Solution


@pytest.mark.parametrize("head, output", [([1, 0, 1], 5), ([0], 0)])
class TestSolution:
    def test_getDecimalValue(self, head: ListNode, output: int):
        sc = Solution()
        assert (
            sc.getDecimalValue(
                head,
            )
            == output
        )

import pytest
from q_1019_nextGreaterNodeInLinkedList import Solution


@pytest.mark.parametrize(
    "head, output", [([2, 1, 5], [5, 5, 0]), ([2, 7, 4, 3, 5], [7, 0, 5, 5, 0])]
)
class TestSolution:
    def test_nextLargerNodes(self, head: Optional[ListNode], output: List[int]):
        sc = Solution()
        assert (
            sc.nextLargerNodes(
                head,
            )
            == output
        )

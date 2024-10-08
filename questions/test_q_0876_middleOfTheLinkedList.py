import pytest
from q_0876_middleOfTheLinkedList import Solution


@pytest.mark.parametrize(
    "head, output", [([1, 2, 3, 4, 5], [3, 4, 5]), ([1, 2, 3, 4, 5, 6], [4, 5, 6])]
)
class TestSolution:
    def test_middleNode(self, head: Optional[ListNode], output: Optional[ListNode]):
        sc = Solution()
        assert (
            sc.middleNode(
                head,
            )
            == output
        )

import pytest
from q_2807_insertGreatestCommonDivisorsInLinkedList import Solution


@pytest.mark.parametrize(
    "head, output", [([18, 6, 10, 3], [18, 6, 6, 2, 10, 1, 3]), ([7], [7])]
)
class TestSolution:
    def test_insertGreatestCommonDivisors(
        self, head: Optional[ListNode], output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.insertGreatestCommonDivisors(
                head,
            )
            == output
        )

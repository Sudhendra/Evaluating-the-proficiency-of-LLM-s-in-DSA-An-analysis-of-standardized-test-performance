import pytest
from q_2816_doubleANumberRepresentedAsALinkedList import Solution


@pytest.mark.parametrize(
    "head, output", [([1, 8, 9], [3, 7, 8]), ([9, 9, 9], [1, 9, 9, 8])]
)
class TestSolution:
    def test_doubleIt(self, head: Optional[ListNode], output: Optional[ListNode]):
        sc = Solution()
        assert (
            sc.doubleIt(
                head,
            )
            == output
        )

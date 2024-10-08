import pytest
from q_0203_removeLinkedListElements import Solution


@pytest.mark.parametrize(
    "head, val, output",
    [([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]), ([], 1, []), ([7, 7, 7, 7], 7, [])],
)
class TestSolution:
    def test_removeElements(
        self, head: Optional[ListNode], val: int, output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.removeElements(
                head,
                val,
            )
            == output
        )

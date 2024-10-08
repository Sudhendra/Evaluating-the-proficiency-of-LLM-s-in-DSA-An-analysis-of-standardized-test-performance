import pytest
from q_0725_splitLinkedListInParts import Solution


@pytest.mark.parametrize(
    "head, k, output",
    [
        ([1, 2, 3], 5, [[1], [2], [3], [], []]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
    ],
)
class TestSolution:
    def test_splitListToParts(
        self, head: Optional[ListNode], k: int, output: List[Optional[ListNode]]
    ):
        sc = Solution()
        assert (
            sc.splitListToParts(
                head,
                k,
            )
            == output
        )

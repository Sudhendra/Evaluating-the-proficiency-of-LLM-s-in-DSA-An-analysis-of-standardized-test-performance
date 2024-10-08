import pytest
from q_2569_handlingSumQueriesAfterUpdate import Solution


@pytest.mark.parametrize(
    "nums1, nums2, queries, output",
    [
        ([1, 0, 1], [0, 0, 0], [[1, 1, 1], [2, 1, 0], [3, 0, 0]], [3]),
        ([1], [5], [[2, 0, 0], [3, 0, 0]], [5]),
    ],
)
class TestSolution:
    def test_handleQuery(
        self,
        nums1: List[int],
        nums2: List[int],
        queries: List[List[int]],
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.handleQuery(
                nums1,
                nums2,
                queries,
            )
            == output
        )

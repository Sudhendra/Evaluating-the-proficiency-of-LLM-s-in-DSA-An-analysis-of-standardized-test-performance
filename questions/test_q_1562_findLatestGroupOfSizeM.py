import pytest
from q_1562_findLatestGroupOfSizeM import Solution


@pytest.mark.parametrize(
    "arr, m, output", [([3, 5, 1, 2, 4], 1, 4), ([3, 1, 5, 4, 2], 2, -1)]
)
class TestSolution:
    def test_findLatestStep(self, arr: List[int], m: int, output: int):
        sc = Solution()
        assert (
            sc.findLatestStep(
                arr,
                m,
            )
            == output
        )

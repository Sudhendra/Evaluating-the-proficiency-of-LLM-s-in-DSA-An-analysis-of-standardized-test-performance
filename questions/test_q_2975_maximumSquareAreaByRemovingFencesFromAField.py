import pytest
from q_2975_maximumSquareAreaByRemovingFencesFromAField import Solution


@pytest.mark.parametrize(
    "m, n, hFences, vFences, output", [(4, 3, [2, 3], [2], 4), (6, 7, [2], [4], -1)]
)
class TestSolution:
    def test_maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.maximizeSquareArea(
                m,
                n,
                hFences,
                vFences,
            )
            == output
        )

import pytest
from q_1552_magneticForceBetweenTwoBalls import Solution


@pytest.mark.parametrize(
    "position, m, output",
    [([1, 2, 3, 4, 7], 3, 3), ([5, 4, 3, 2, 1, 1000000000], 2, 999999999)],
)
class TestSolution:
    def test_maxDistance(self, position: List[int], m: int, output: int):
        sc = Solution()
        assert (
            sc.maxDistance(
                position,
                m,
            )
            == output
        )

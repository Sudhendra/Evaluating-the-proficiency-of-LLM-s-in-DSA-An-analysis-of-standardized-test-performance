import pytest
from q_0458_poorPigs import Solution


@pytest.mark.parametrize(
    "buckets, minutesToDie, minutesToTest, output", [(4, 15, 15, 2), (4, 15, 30, 2)]
)
class TestSolution:
    def test_poorPigs(
        self, buckets: int, minutesToDie: int, minutesToTest: int, output: int
    ):
        sc = Solution()
        assert (
            sc.poorPigs(
                buckets,
                minutesToDie,
                minutesToTest,
            )
            == output
        )

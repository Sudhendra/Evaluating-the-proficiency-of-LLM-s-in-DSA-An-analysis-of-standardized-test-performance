import pytest
from q_0514_freedomTrail import Solution


@pytest.mark.parametrize(
    "ring, key, output", [("godding", "gd", 4), ("godding", "godding", 13)]
)
class TestSolution:
    def test_findRotateSteps(self, ring: str, key: str, output: int):
        sc = Solution()
        assert (
            sc.findRotateSteps(
                ring,
                key,
            )
            == output
        )

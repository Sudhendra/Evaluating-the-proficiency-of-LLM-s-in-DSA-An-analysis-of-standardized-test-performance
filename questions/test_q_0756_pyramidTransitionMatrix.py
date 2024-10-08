import pytest
from q_0756_pyramidTransitionMatrix import Solution


@pytest.mark.parametrize(
    "bottom, allowed, output",
    [
        ("BCD", ["BCC", "CDE", "CEA", "FFF"], True),
        ("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"], False),
    ],
)
class TestSolution:
    def test_pyramidTransition(self, bottom: str, allowed: List[str], output: bool):
        sc = Solution()
        assert (
            sc.pyramidTransition(
                bottom,
                allowed,
            )
            == output
        )

import pytest
from q_2434_usingARobotToPrintTheLexicographicallySmallestString import Solution


@pytest.mark.parametrize(
    "s, output", [("zza", "azz"), ("bac", "abc"), ("bdda", "addb")]
)
class TestSolution:
    def test_robotWithString(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.robotWithString(
                s,
            )
            == output
        )

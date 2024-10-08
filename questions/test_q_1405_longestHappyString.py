import pytest
from q_1405_longestHappyString import Solution


@pytest.mark.parametrize("a, b, c, output", [(1, 1, 7, "ccaccbcc"), (7, 1, 0, "aabaa")])
class TestSolution:
    def test_longestDiverseString(self, a: int, b: int, c: int, output: str):
        sc = Solution()
        assert (
            sc.longestDiverseString(
                a,
                b,
                c,
            )
            == output
        )

import pytest
from q_1844_replaceAllDigitsWithCharacters import Solution


@pytest.mark.parametrize(
    "s, output", [("a1c1e1", "abcdef"), ("a1b2c3d4e", "abbdcfdhe")]
)
class TestSolution:
    def test_replaceDigits(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.replaceDigits(
                s,
            )
            == output
        )

import pytest
from q_0299_bullsAndCows import Solution


@pytest.mark.parametrize(
    "secret, guess, output", [("1807", "7810", "1A3B"), ("1123", "0111", "1A1B")]
)
class TestSolution:
    def test_getHint(self, secret: str, guess: str, output: str):
        sc = Solution()
        assert (
            sc.getHint(
                secret,
                guess,
            )
            == output
        )

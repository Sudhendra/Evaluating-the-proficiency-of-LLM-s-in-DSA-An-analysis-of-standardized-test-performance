import pytest
from q_1189_maximumNumberOfBalloons import Solution


@pytest.mark.parametrize(
    "text, output", [("nlaebolko", 1), ("loonbalxballpoon", 2), ("leetcode", 0)]
)
class TestSolution:
    def test_maxNumberOfBalloons(self, text: str, output: int):
        sc = Solution()
        assert (
            sc.maxNumberOfBalloons(
                text,
            )
            == output
        )

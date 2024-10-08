import pytest
from q_2390_removingStarsFromAString import Solution


@pytest.mark.parametrize("s, output", [("leet**cod*e", "lecoe"), ("erase*****", "")])
class TestSolution:
    def test_removeStars(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.removeStars(
                s,
            )
            == output
        )

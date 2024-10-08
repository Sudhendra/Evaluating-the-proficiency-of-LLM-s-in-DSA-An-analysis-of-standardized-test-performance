import pytest
from q_1781_sumOfBeautyOfAllSubstrings import Solution


@pytest.mark.parametrize("s, output", [("aabcb", 5), ("aabcbaa", 17)])
class TestSolution:
    def test_beautySum(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.beautySum(
                s,
            )
            == output
        )

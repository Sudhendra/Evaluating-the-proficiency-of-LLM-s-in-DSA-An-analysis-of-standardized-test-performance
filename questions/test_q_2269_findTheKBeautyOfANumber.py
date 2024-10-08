import pytest
from q_2269_findTheKBeautyOfANumber import Solution


@pytest.mark.parametrize("num, k, output", [(240, 2, 2), (430043, 2, 2)])
class TestSolution:
    def test_divisorSubstrings(self, num: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.divisorSubstrings(
                num,
                k,
            )
            == output
        )

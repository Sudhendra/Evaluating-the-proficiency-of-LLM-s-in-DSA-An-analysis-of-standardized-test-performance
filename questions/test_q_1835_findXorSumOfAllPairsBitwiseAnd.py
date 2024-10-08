import pytest
from q_1835_findXorSumOfAllPairsBitwiseAnd import Solution


@pytest.mark.parametrize("arr1, arr2, output", [([1, 2, 3], [6, 5], 0), ([12], [4], 4)])
class TestSolution:
    def test_getXORSum(self, arr1: List[int], arr2: List[int], output: int):
        sc = Solution()
        assert (
            sc.getXORSum(
                arr1,
                arr2,
            )
            == output
        )

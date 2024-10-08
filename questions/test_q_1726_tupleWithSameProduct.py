import pytest
from q_1726_tupleWithSameProduct import Solution


@pytest.mark.parametrize("nums, output", [([2, 3, 4, 6], 8), ([1, 2, 4, 5, 10], 16)])
class TestSolution:
    def test_tupleSameProduct(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.tupleSameProduct(
                nums,
            )
            == output
        )

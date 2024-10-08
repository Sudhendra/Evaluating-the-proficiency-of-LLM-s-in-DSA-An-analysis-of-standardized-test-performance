import pytest
from q_0898_bitwiseOrsOfSubarrays import Solution


@pytest.mark.parametrize("arr, output", [([0], 1), ([1, 1, 2], 3), ([1, 2, 4], 6)])
class TestSolution:
    def test_subarrayBitwiseORs(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.subarrayBitwiseORs(
                arr,
            )
            == output
        )

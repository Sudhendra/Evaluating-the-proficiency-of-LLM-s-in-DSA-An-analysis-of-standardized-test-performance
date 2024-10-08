import pytest
from q_1338_reduceArraySizeToTheHalf import Solution


@pytest.mark.parametrize(
    "arr, output", [([3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2), ([7, 7, 7, 7, 7, 7], 1)]
)
class TestSolution:
    def test_minSetSize(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.minSetSize(
                arr,
            )
            == output
        )

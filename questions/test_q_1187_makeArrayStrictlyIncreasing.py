import pytest
from q_1187_makeArrayStrictlyIncreasing import Solution


@pytest.mark.parametrize(
    "arr1, arr2, output",
    [
        ([1, 5, 3, 6, 7], [1, 3, 2, 4], 1),
        ([1, 5, 3, 6, 7], [4, 3, 1], 2),
        ([1, 5, 3, 6, 7], [1, 6, 3, 3], -1),
    ],
)
class TestSolution:
    def test_makeArrayIncreasing(self, arr1: List[int], arr2: List[int], output: int):
        sc = Solution()
        assert (
            sc.makeArrayIncreasing(
                arr1,
                arr2,
            )
            == output
        )

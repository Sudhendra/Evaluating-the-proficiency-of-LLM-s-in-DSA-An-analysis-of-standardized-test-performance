import pytest
from q_1073_addingTwoNegabinaryNumbers import Solution


@pytest.mark.parametrize(
    "arr1, arr2, output",
    [([1, 1, 1, 1, 1], [1, 0, 1], [1, 0, 0, 0, 0]), ([0], [0], [0]), ([0], [1], [1])],
)
class TestSolution:
    def test_addNegabinary(self, arr1: List[int], arr2: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.addNegabinary(
                arr1,
                arr2,
            )
            == output
        )

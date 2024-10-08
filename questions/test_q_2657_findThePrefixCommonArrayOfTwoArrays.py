import pytest
from q_2657_findThePrefixCommonArrayOfTwoArrays import Solution


@pytest.mark.parametrize(
    "A, B, output",
    [([1, 3, 2, 4], [3, 1, 2, 4], [0, 2, 3, 4]), ([2, 3, 1], [3, 1, 2], [0, 1, 3])],
)
class TestSolution:
    def test_findThePrefixCommonArray(
        self, A: List[int], B: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findThePrefixCommonArray(
                A,
                B,
            )
            == output
        )

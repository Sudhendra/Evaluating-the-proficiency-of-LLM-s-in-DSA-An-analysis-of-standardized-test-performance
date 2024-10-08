import pytest
from q_2766_relocateMarbles import Solution


@pytest.mark.parametrize(
    "nums, moveFrom, moveTo, output",
    [
        ([1, 6, 7, 8], [1, 7, 2], [2, 9, 5], [5, 6, 8, 9]),
        ([1, 1, 3, 3], [1, 3], [2, 2], [2]),
    ],
)
class TestSolution:
    def test_relocateMarbles(
        self, nums: List[int], moveFrom: List[int], moveTo: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.relocateMarbles(
                nums,
                moveFrom,
                moveTo,
            )
            == output
        )

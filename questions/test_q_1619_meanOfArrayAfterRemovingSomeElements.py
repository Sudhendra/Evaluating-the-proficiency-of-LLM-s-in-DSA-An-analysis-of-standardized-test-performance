import pytest
from q_1619_meanOfArrayAfterRemovingSomeElements import Solution


@pytest.mark.parametrize(
    "arr, output",
    [
        ([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3], 2.0),
        ([6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0], 4.0),
        (
            [
                6,
                0,
                7,
                0,
                7,
                5,
                7,
                8,
                3,
                4,
                0,
                7,
                8,
                1,
                6,
                8,
                1,
                1,
                2,
                4,
                8,
                1,
                9,
                5,
                4,
                3,
                8,
                5,
                10,
                8,
                6,
                6,
                1,
                0,
                6,
                10,
                8,
                2,
                3,
                4,
            ],
            4.77778,
        ),
    ],
)
class TestSolution:
    def test_trimMean(self, arr: List[int], output: float):
        sc = Solution()
        assert (
            sc.trimMean(
                arr,
            )
            == output
        )

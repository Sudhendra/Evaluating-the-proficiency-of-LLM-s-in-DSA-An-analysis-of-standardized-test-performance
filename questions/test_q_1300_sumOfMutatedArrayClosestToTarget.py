import pytest
from q_1300_sumOfMutatedArrayClosestToTarget import Solution


@pytest.mark.parametrize(
    "arr, target, output",
    [
        ([4, 9, 3], 10, 3),
        ([2, 3, 5], 10, 5),
        ([60864, 25176, 27249, 21296, 20204], 56803, 11361),
    ],
)
class TestSolution:
    def test_findBestValue(self, arr: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.findBestValue(
                arr,
                target,
            )
            == output
        )

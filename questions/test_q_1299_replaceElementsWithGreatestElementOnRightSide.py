import pytest
from q_1299_replaceElementsWithGreatestElementOnRightSide import Solution


@pytest.mark.parametrize(
    "arr, output", [([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]), ([400], [-1])]
)
class TestSolution:
    def test_replaceElements(self, arr: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.replaceElements(
                arr,
            )
            == output
        )

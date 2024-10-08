import pytest
from q_0817_linkedListComponents import Solution


@pytest.mark.parametrize(
    "head, nums, output",
    [([0, 1, 2, 3], [0, 1, 3], 2), ([0, 1, 2, 3, 4], [0, 3, 1, 4], 2)],
)
class TestSolution:
    def test_numComponents(
        self, head: Optional[ListNode], nums: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.numComponents(
                head,
                nums,
            )
            == output
        )

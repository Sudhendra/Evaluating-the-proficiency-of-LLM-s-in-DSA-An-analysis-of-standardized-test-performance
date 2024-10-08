import pytest
from q_1720_decodeXoredArray import Solution


@pytest.mark.parametrize(
    "encoded, first, output",
    [([1, 2, 3], 1, [1, 0, 2, 1]), ([6, 2, 7, 3], 4, [4, 2, 0, 7, 4])],
)
class TestSolution:
    def test_decode(self, encoded: List[int], first: int, output: List[int]):
        sc = Solution()
        assert (
            sc.decode(
                encoded,
                first,
            )
            == output
        )

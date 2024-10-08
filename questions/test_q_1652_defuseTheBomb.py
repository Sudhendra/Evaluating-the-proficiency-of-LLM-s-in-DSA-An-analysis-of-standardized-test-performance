import pytest
from q_1652_defuseTheBomb import Solution


@pytest.mark.parametrize(
    "code, k, output",
    [
        ([5, 7, 1, 4], 3, [12, 10, 16, 13]),
        ([1, 2, 3, 4], 0, [0, 0, 0, 0]),
        ([2, 4, 9, 3], -2, [12, 5, 6, 13]),
    ],
)
class TestSolution:
    def test_decrypt(self, code: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.decrypt(
                code,
                k,
            )
            == output
        )

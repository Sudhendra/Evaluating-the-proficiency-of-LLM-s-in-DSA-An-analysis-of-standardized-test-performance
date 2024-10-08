import pytest
from q_1494_parallelCoursesIi import Solution


@pytest.mark.parametrize(
    "n, relations, k, output",
    [(4, [[2, 1], [3, 1], [1, 4]], 2, 3), (5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2, 4)],
)
class TestSolution:
    def test_minNumberOfSemesters(
        self, n: int, relations: List[List[int]], k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minNumberOfSemesters(
                n,
                relations,
                k,
            )
            == output
        )

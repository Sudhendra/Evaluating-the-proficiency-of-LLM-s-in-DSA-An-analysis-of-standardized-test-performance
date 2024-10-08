import pytest
from q_2126_destroyingAsteroids import Solution


@pytest.mark.parametrize(
    "mass, asteroids, output",
    [(10, [3, 9, 19, 5, 21], True), (5, [4, 9, 23, 4], False)],
)
class TestSolution:
    def test_asteroidsDestroyed(self, mass: int, asteroids: List[int], output: bool):
        sc = Solution()
        assert (
            sc.asteroidsDestroyed(
                mass,
                asteroids,
            )
            == output
        )

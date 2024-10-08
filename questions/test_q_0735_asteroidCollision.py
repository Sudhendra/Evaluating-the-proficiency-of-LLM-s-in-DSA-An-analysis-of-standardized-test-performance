import pytest
from q_0735_asteroidCollision import Solution


@pytest.mark.parametrize(
    "asteroids, output", [([5, 10, -5], [5, 10]), ([8, -8], []), ([10, 2, -5], [10])]
)
class TestSolution:
    def test_asteroidCollision(self, asteroids: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.asteroidCollision(
                asteroids,
            )
            == output
        )

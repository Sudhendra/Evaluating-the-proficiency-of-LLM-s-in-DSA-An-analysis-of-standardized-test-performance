import pytest
from q_2525_categorizeBoxAccordingToCriteria import Solution


@pytest.mark.parametrize(
    "length, width, height, mass, output",
    [(1000, 35, 700, 300, "Heavy"), (200, 50, 800, 50, "Neither")],
)
class TestSolution:
    def test_categorizeBox(
        self, length: int, width: int, height: int, mass: int, output: str
    ):
        sc = Solution()
        assert (
            sc.categorizeBox(
                length,
                width,
                height,
                mass,
            )
            == output
        )

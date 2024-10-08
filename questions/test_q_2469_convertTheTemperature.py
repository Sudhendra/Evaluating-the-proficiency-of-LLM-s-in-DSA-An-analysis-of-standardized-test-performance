import pytest
from q_2469_convertTheTemperature import Solution


@pytest.mark.parametrize(
    "celsius, output", [(36.5, [309.65, 97.7]), (122.11, [395.26, 251.798])]
)
class TestSolution:
    def test_convertTemperature(self, celsius: float, output: List[float]):
        sc = Solution()
        assert (
            sc.convertTemperature(
                celsius,
            )
            == output
        )

import pytest
from q_0504_base7 import Solution


@pytest.mark.parametrize("num, output", [(100, "202"), (-7, "-10")])
class TestSolution:
    def test_convertToBase7(self, num: int, output: str):
        sc = Solution()
        assert (
            sc.convertToBase7(
                num,
            )
            == output
        )

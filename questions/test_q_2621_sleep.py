import pytest
from q_2621_sleep import Solution


@pytest.mark.parametrize("millis, output", [(100, 100), (200, 200)])
class TestSolution:
    def test_sleep(self, output: Any):
        sc = Solution()
        assert (
            sc.sleep(
                millis,
            )
            == output
        )

from import_pandas import loader_csv
import pytest


def test_prepare(benchmark):
    benchmark.pedantic(loader_csv, args=('other_user_logs',), iterations=3, rounds=2, warmup_rounds=1)


if __name__ == '__main__':
    pytest.main()

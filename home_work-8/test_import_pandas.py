from import_pandas import csv_loader
import pytest


def test_prepare(benchmark):
    benchmark.pedantic(csv_loader, args=('other_user_logs',), iterations=10, rounds=5, warmup_rounds=2)


if __name__ == '__main__':
    pytest.main()

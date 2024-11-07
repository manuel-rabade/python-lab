# pytest demo

```
poetry add --group dev pytest
poetry run pytest

poetry run pytest -m slow
poetry run pytest -m 'not slow'
poetry run pytest -v ./tests/test_functions/test_mark.py::test_params

poetry run pytest -v --cov-report term-missing --cov pytest_demo
poetry run pytest -v --cov-report term-missing --cov pytest_demo -m strings
```

- https://medium.com/engineered-publicis-sapient/testing-python-code-with-pytest-a-quickstart-guide-36f8da3d402
  - https://docs.pytest.org/en/stable/how-to/mark.html

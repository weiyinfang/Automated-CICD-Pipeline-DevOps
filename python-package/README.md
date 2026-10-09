# tempconv

`tempconv` converts temperatures between Celsius, Fahrenheit and Kelvin.

```python
from tempconv.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
)

celsius_to_fahrenheit(100)  # 212.0
fahrenheit_to_celsius(32)   # 0.0
celsius_to_kelvin(0)        # 273.15
```

Every function takes an `int` or `float` and returns a `float`. A string raises `TypeError`.

The package is linted, tested, versioned and published by the GitLab CI/CD pipeline in
`.gitlab-ci.yml`. The pipeline, the release process and the required CI/CD variables are described
in the repository's main README:
https://github.com/weiyinfang/Automated-CICD-Pipeline-DevOps

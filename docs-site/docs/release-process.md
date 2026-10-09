# Release process

Releases are driven by Git tags. The package pipeline runs four stages:

| Stage | What it does |
|-------|--------------|
| `lint` | Pylint on the package and tests |
| `test` | Pytest with a coverage report |
| `build` | Validates the tag as `x.y.z` or `x.y.z+local`, writes it into `pyproject.toml` and builds the sdist and wheel |
| `publish` | Uploads the build to Google Artifact Registry (tag pipelines only) |

To release version `1.2.3`:

```bash
git tag 1.2.3
git push origin 1.2.3
```

!!! note
    The tag must be an `x.y.z` version, optionally with a local version
    suffix such as `1.0.0+65q130`. Tags such as `v1.2.3` fail the `build`
    stage and nothing is published.

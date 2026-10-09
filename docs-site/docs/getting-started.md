# Getting started

## Requirements

- Python 3.10 or newer

## Install from source

```bash
git clone <repository-url>
cd <repository>/python-package
pip install .
```

## Install from Google Artifact Registry

Released versions are published to a Python repository in Google Artifact
Registry. Install the keyring backend, authenticate with Google Cloud, then
install the package:

```bash
pip install keyrings.google-artifactregistry-auth
gcloud auth application-default login
pip install --index-url https://<location>-python.pkg.dev/<project-id>/<repository>/simple/ tempconv
```

## First conversion

```python
from tempconv.converter import celsius_to_fahrenheit, celsius_to_kelvin

print(celsius_to_fahrenheit(37))  # 98.6
print(celsius_to_kelvin(-273.15))  # 0.0
```

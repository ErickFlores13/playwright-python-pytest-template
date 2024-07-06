# Playwright + Python + pytest Template

## Setup

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run Playwright to install browser binaries:
    ```bash
    playwright install
    ```
4. Create a `.env` file with the necessary environment variables using `.env.example` as a template.

## Running Tests

To run the tests, use:
```bash
pytest
```

To generate a HTML report, use:
```bash
pytest --html=report.html --self-contained-html
```

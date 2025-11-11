# Wellarchitect Test - Vulnerable Python Application

This is a **deliberately vulnerable** Python application created for testing security scanning tools, specifically the "Reachable CVEs" feature.

## ⚠️ WARNING
This application contains known security vulnerabilities. **DO NOT** deploy this to production or use it in any real-world scenario.

## Vulnerable Dependencies

This project includes the following packages with known CVEs:

- **requests==2.25.0** - CVE-2021-33503 (Cookie injection)
- **flask==1.1.1** - CVE-2023-30861 (DOS), CVE-2019-1010083 (DOS)
- **urllib3==1.25.8** - CVE-2021-33503 (HTTP request smuggling), CVE-2020-26137
- **pyyaml==5.3.1** - CVE-2020-14343 (Arbitrary code execution via yaml.load)
- **jinja2==2.11.2** - CVE-2020-28493 (RCE via SSTI)
- **cryptography==2.9** - CVE-2020-25659, CVE-2020-36242

## Active Usage

All vulnerable packages are **actively imported and used** in the codebase:

### `app.py`
- Imports: `requests`, `flask`, `urllib3`, `yaml`, `jinja2`
- Uses requests for HTTP calls
- Uses Flask for web framework
- Uses Jinja2 for template rendering (with SSTI vulnerability)
- Uses PyYAML with unsafe `yaml.load()`

### `utils.py`
- Imports: `requests`, `yaml`, `cryptography`
- File downloads with requests
- YAML parsing with vulnerable `yaml.load()`
- Weak encryption with cryptography

### `api_client.py`
- Imports: `requests`, `urllib3`
- REST API client using requests
- Connection pooling with urllib3

### `config_loader.py`
- Imports: `yaml`
- Configuration loading with vulnerable YAML parsing

## Expected Test Results

When scanned with the Wellarchitect security scanner:

1. **SBOM nodes**: Should create `sbom/package` nodes for all 6 packages
2. **CVE nodes**: Should create `security/cve` nodes for multiple high/critical CVEs
3. **Import edges**: Should create `file → imports → package` edges for Python files
4. **Reachable CVE finding**: Should emit an aggregate "Reachable CVEs" finding linking:
   - Vulnerable packages (from SBOM)
   - High/critical CVEs (from Trivy)
   - Python files that import those packages

## Usage

**DO NOT run this application in production!**

For testing purposes only:

```bash
# Install dependencies (in a virtual environment!)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run the app (for testing only!)
python app.py
```

## License

This is a test repository for security scanning validation. Not licensed for production use.


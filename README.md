# SecureFlow-CI-CD

## 📌 About the Project

**SecureFlow-CI-CD** demonstrates a CI/CD pipeline using GitHub Actions to perform security checks and analyses on a Python project. The workflow steps include:

- **Linting** (_flake8_).
- **Unit Testing** (_pytest_).
- **Security Analysis** (_CodeQL_ for vulnerability detection).
- **Security Scanning** (_Bandit_, intentionally configured to fail).

The project contains a small Streamlit application (`bg_remove.py`) for image background removal, accompanied by example tests in `tests/test_bg_remove.py`.

> **Note**: The _Bandit Scan_ intentionally fails due to purposely included insecure patterns (such as the use of `assert`). This demonstrates how the pipeline handles security failures.

---

## 🛠️ Requirements

To use or test **SecureFlow-CI-CD**, install the following tools:

- [Git](https://git-scm.com/)  
- [Python 3.11+](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/)  

To run the Streamlit application locally, install the dependencies listed in `requirements.txt`.

---

## 📥 How to Test the Workflow

### 🔹 1. Initial Setup

1. **Fork** this repository to your GitHub.
2. **Enable GitHub Actions** on your fork (_Actions → Enable workflows_, if necessary).
3. **Edit or push** to the `main` branch to trigger the workflow (`.github/workflows/ci-cd.yml`).
4. **Check the results** in the repository's _Actions_ tab.

### 🔹 2. Job Execution

1. **Lint (`flake8`)** – Checks `bg_remove.py`. If there are errors, the step will fail.  
2. **Tests (`pytest`)** – Runs the tests in `tests/`. If there are failures, the job will fail.  
3. **CodeQL** – Analyzes the code for vulnerabilities. Alerts appear in the _Security_ tab.  
4. **Bandit Scan** – Scans the code for security issues (`bandit -r .`). **This job intentionally fails** due to insecure patterns included in the code.  

> The workflow will succeed in all steps except for the **Bandit Scan**, which will demonstrate security issues.

---

## 📝 Additional Details

- **bg_remove.py** – Streamlit application for image background removal (`rembg`, `Pillow`).
- **tests/test_bg_remove.py** – Example tests using `pytest`.
- **requirements.txt** – Lists the project dependencies.
- **.github/workflows/ci-cd.yml** – CI/CD pipeline configuration.
- **Online Demo** – Access the application at [RemoveBG Streamlit](https://removebg-gabriel-lopes.streamlit.app/).

---

## 🛡️ Why Does Bandit Fail?

The code contains intentional vulnerabilities for Bandit to detect and demonstrate how the workflow handles security failures. The pipeline is structured to pass Lint, Tests, and CodeQL checks but fail the Bandit Scan.

---

## 👨‍💻 Contributing

Feel free to **fork, open issues, or submit pull requests**. The project was developed to demonstrate secure practices in CI/CD and automated security analysis.

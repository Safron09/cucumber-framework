# Cucumber-UI-Framework

A BDD UI test automation framework built with Behave (Python Cucumber), Selenium WebDriver, and Allure reporting. Test scenarios are written in Gherkin and executed against a web application using a Page Object Model structure. Designed for GitLab CI/CD integration with full Allure report publishing.

---

## What This Framework Does

- BDD test scenarios written in Gherkin (`.feature` files) — readable by non-engineers
- Step definitions backed by a Page Object layer — no raw Selenium in step files
- Multi-browser support — Chrome, Chrome headless, Firefox
- Allure report generated as a GitLab pipeline artifact after every run
- CI/CD via GitLab — triggers on every push to `main` and every merge request

---

## Project Structure

```
Cucumber-UI-Framework/
├── features/
│   ├── pages/                   # Page Object layer
│   │   ├── base_page.py         # Shared Selenium wait utilities
│   │   ├── registration_page.py # Registration flow page object
│   │   └── login_page.py        # Login flow page object
│   ├── steps/                   # Step definitions (Gherkin → Python)
│   │   ├── new_player.py        # Registration steps
│   │   └── login.py             # Login steps
│   ├── test/                    # Gherkin feature files
│   │   ├── new_player.feature   # New player registration scenarios
│   │   └── login.feature        # Player login scenarios
│   └── environment.py           # Behave hooks — browser setup/teardown
├── allure-results/              # Allure output (git-ignored)
├── .gitlab-ci.yml               # GitLab CI pipeline
├── behave.ini                   # Behave configuration
├── .env.example                 # Required environment variable reference
└── requirements.txt             # Pinned Python dependencies
```

---

## Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.11 |
| BDD Framework | Behave (Cucumber for Python) |
| Browser Automation | Selenium WebDriver 4 |
| Reporting | Allure |
| CI/CD | GitLab CI |

---

## Architecture Decisions

**Gherkin feature files** — scenarios are written in plain English in `.feature` files. This keeps test intent visible to product owners and non-technical stakeholders, not just engineers.

**Page Object Model** — `features/pages/` contains one class per page. Locators and interactions are defined once and reused across all step files. Steps call page methods, never Selenium directly.

**`base_page.py`** — all page objects inherit from `BasePage`, which wraps Selenium's `WebDriverWait` into readable methods (`find`, `click`, `type_text`, `is_element_visible`). Explicit waits are enforced throughout — no `sleep()`.

**Allure reporting** — `allure-behave` formatter outputs structured results to `allure-results/`. The GitLab pipeline generates and publishes the HTML report as a downloadable artifact on every run.

---

## How to Run

### Prerequisites

```bash
pip install -r requirements.txt
```

### Environment setup

```bash
cp .env.example .env
# Fill in BASE_URL and BROWSER
```

### Run all scenarios

```bash
behave features/test/
```

### Run with Allure reporting

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results features/test/
allure serve allure-results
```

### Run by tag

```bash
behave --tags=@registration features/test/
behave --tags=@login features/test/
```

### Run headless (CI mode)

```bash
BROWSER=chrome_headless behave features/test/
```

---

## CI/CD Pipeline

The `.gitlab-ci.yml` defines two stages:

1. **test** — installs dependencies, runs the full Behave suite with Allure formatter, uploads `allure-results/` as an artifact
2. **report** — generates the Allure HTML report from results and publishes it as a downloadable artifact

Triggers on every push to `main` and every merge request. Failures block the pipeline.

---

## Author

**Yuriy Safronnynov** — Senior SDET / QA Automation Architect

https://www.linkedin.com/in/yuriy-safronnynov/ | https://github.com/Safron09

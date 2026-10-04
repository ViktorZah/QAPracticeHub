# QA Practice Hub – Selenium Test Automation

An end-to-end UI test automation project for [QA Practice Hub](https://qapracticehub.com), built with **Python**, **Selenium WebDriver** and **pytest**. It uses the **Page Object Model (POM)** to keep tests short, readable and easy to maintain.

## What's covered

Each section of the practice site has its own page object and test module:

| Section | Page object | Tests | pytest marker |
|---|---|---|---|
| Inputs (text, email, number, date, time, phone, read-only, disabled, ...) | `inputs_page.py` | `test_inputs.py` | `inputs` |
| Forms (login, password visibility, forgot password, registration) | `forms_page.py` | `test_forms.py` | `forms` |
| OTP Login (fetch, submit, expiry, resend) | `otp_login_page.py` | `test_otp_login.py` | `otp` |
| Selection (radio buttons, checkboxes, dropdowns, listbox, toggle, autocomplete) | `selection_page.py` | `test_selection.py` | `select` |
| Buttons (click, double click, right click, hover, popup, ...) | `buttons_page.py` | `test_buttons.py` | `buttons` |
| Tables (filter, sort, select, add and remove rows) | `tables_page.py` | `test_tables.py` | `tables` |
| Changing Attributes (dynamic IDs, timestamps, countdown, dynamic links) | `changing_atr_page.py` | `test_changing_atrs.py` | `changing_attributes` |
| Side bar navigation | `components/navbar.py` | `test_navigation_tab.py` | – |

## Project structure

```
QA Practice Hub/
├── config.ini              # Base URL of the site under test
├── pytest.ini              # pytest settings and registered markers
├── requirements.txt        # Python dependencies
├── pages/                  # Page Object Model
│   ├── base_page.py        # Shared helpers: waits, clicks, typing, alerts, actions
│   ├── home_page.py        # Entry point; exposes the navbar and every section page
│   ├── components/
│   │   └── navbar.py       # Side bar navigation component
│   ├── inputs_page.py
│   ├── forms_page.py
│   ├── otp_login_page.py
│   ├── selection_page.py
│   ├── buttons_page.py
│   ├── tables_page.py
│   └── changing_atr_page.py
├── tests/
│   ├── conftest.py         # `driver` and `home_page` fixtures
│   └── test_*.py           # One test module per site section
└── utils/
    ├── config_reader.py    # Reads values from config.ini
    └── driver_factory.py   # Chrome driver builder (headless option)
```

## How it works

- **`BasePage`** wraps Selenium with explicit waits (`WebDriverWait`) and reusable actions: `click`, `type_text`, `get_text`, double/right click, hover, alert handling, tab switching and more. Every page object inherits from it.
- **`HomePage`** loads the site and gives tests access to the `navbar` and each section (`inputs_tab`, `form_tab`, `otp_login_tab`, `selection_tab`, `buttons_tab`, `tables_tab`, `changing_attr_tab`).
- **`conftest.py`** provides two fixtures: `driver` (starts and quits Chrome around each test) and `home_page` (a driver already pointed at the site).
- Locators live in the page objects, so tests contain only the scenario and the assertions.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/ViktorZah/QAPracticeHub.git
cd QAPracticeHub
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows: `.venv\Scripts\activate`

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Make sure Google Chrome is installed

No manual ChromeDriver setup is needed.

## Running the tests

Run everything from the project root (the config file is read relative to it):

```bash
pytest
```
Available markers: `inputs`, `forms`, `otp`, `select`, `buttons`, `tables`, `changing_attributes` (and `smoke`, registered for quick-test selection).

## Configuration

The site under test is set in `config.ini`:

```ini
[API_SETTINGS]
base_url = https://qapracticehub.com
```

Change `base_url` to point the suite at another environment.

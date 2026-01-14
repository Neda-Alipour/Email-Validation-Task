# Email Validation Task

## Overview

This project implements a simple email validation system using Python. It checks whether a given email address follows a valid format based on standard email structure rules. Email validation is commonly used in applications to ensure data quality and prevent invalid user input.

---

## Features

* Validates email address format
* Supports validation of single or multiple email inputs
* Simple and lightweight implementation
* Easy to extend for additional validation rules

---

## Requirements

* Python 3.x

If external libraries are used, they should be listed in `requirements.txt`.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Neda-Alipour/Email-Validation-Task.git
cd Email-Validation-Task
```

(Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

Install dependencies (if applicable):

```bash
pip install -r requirements.txt
```

---

## Usage

### Validate a Single Email

```bash
python validate_email.py user@example.com
```

### Validate a List of Emails

```bash
python batch_validate.py emails.txt
```

Each email will be checked and reported as valid or invalid.

---

## Example

```python
from email_validator import validate_email

email = "example@test.com"

if validate_email(email):
    print("Valid email")
else:
    print("Invalid email")
```

---

## Project Structure

```
Email-Validation-Task/
├── validate_email.py
├── batch_validate.py
├── utils.py
├── tests/
│   └── test_email_validation.py
├── requirements.txt
└── README.md
```

---

## Testing

If tests are included, run them using:

```bash
pytest
```

---

## Possible Improvements

* Domain validation using DNS or MX record checks
* Support for internationalized email addresses
* Integration with web forms or APIs
* Improved error handling and logging

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author

Neda Alipour
GitHub: [https://github.com/Neda-Alipour](https://github.com/Neda-Alipour)

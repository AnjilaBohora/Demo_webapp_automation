# Automation Testing Framework for E-commerce Website using Python Selenium

## Project Overview

This project automates the core functionalities of the **Demo Web Shop** e-commerce website using **Selenium WebDriver**, **Python**, and **PyTest**, following the **Page Object Model (POM)** design pattern.

**Website:** https://demowebshop.tricentis.com

The framework validates major user workflows such as:

* User Registration
* User Login & Logout
* Product Search
* Add to Cart
* Wishlist Management
* Checkout Process
* Newsletter Subscription
* Navigation & UI Validation
* Responsive UI Testing
* Performance Testing using JMeter
* Lighthouse UI & Performance Analysis

The framework is designed to be scalable, reusable, and maintainable while handling dynamic web elements and synchronization issues effectively.

---

## Objectives

* Automate major functionalities of an e-commerce website
* Implement automation using Selenium, PyTest, and POM architecture
* Handle dynamic web elements and page synchronization
* Perform user interaction testing
* Generate test execution reports
* Conduct UI and performance analysis using Lighthouse
* Perform load testing using Apache JMeter
* Develop reusable and maintainable automation scripts

---

## Tools & Technologies

| Tool                 | Details                 |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Automation Tool      | Selenium WebDriver      |
| Test Framework       | PyTest                  |
| Browser              | Google Chrome           |
| Driver Manager       | webdriver-manager       |
| Design Pattern       | Page Object Model (POM) |
| Performance Testing  | Apache JMeter           |
| UI Audit Tool        | Lighthouse              |
| Reporting Tool       | pytest-html             |
| IDE                  | VS Code                 |

---

## Project Structure

```text
DEMOWEBAPP/
│
├── login.py
├── product.py
├── cart.py
├── checkout.py
├── logout.py
│
├── test_webapp.py
├── conftest.py
├── requirements.txt
│
└── reports/
    └── report.html
```

---

## Module Description

### login.py

Handles:

* Open Website
* Click Login
* Enter Email
* Enter Password
* Click Login Button

### product.py

Handles:

* Open Books Category
* Sort Products (Low to High Price)
* Open Product in New Tab
* Add Product to Cart
* Open Shopping Cart

### cart.py

Handles:

* Update Product Quantity
* Remove Product
* Accept Terms of Service
* Proceed to Checkout

### checkout.py

Handles:

* Billing Address
* Shipping Address
* Shipping Method
* Payment Method
* Order Confirmation

### logout.py

Handles:

* Logout Functionality
* Logout Verification

### conftest.py

Contains:

* WebDriver Setup
* Browser Configuration
* PyTest Fixtures

### test_webapp.py

Complete End-to-End Test Flow:

```text
Login
 ↓
Sort Product
 ↓
Open Product in New Tab
 ↓
Add To Cart
 ↓
Update Quantity
 ↓
Remove Product
 ↓
Update Cart
 ↓
Checkout
 ↓
Return to Parent Tab
 ↓
Logout
```

---

## Selenium Concepts Used

* Page Object Model (POM)
* PyTest Fixtures
* Assertions
* Explicit Waits
* Dynamic Content Handling
* Window & Tab Handling
* End-to-End Testing
* Synchronization Techniques

---

## Web Elements Covered

* Text Boxes
* Buttons
* Links
* Checkboxes
* Browser Tabs/Windows
* Forms
* Validation Messages

---

## Test Scenarios

| Test Scenario                 | Status |
| ----------------------------- | ------ |
| User Registration             | ✅ Pass |
| Login Functionality           | ✅ Pass |
| Product Search & Product Page | ❌ Fail |
| Cart Functionality            | ✅ Pass |
| Wishlist Functionality        | ❌ Fail |
| Checkout Process              | ✅ Pass |
| Newsletter Subscription       | ✅ Pass |
| Responsive UI Testing         | ✅ Pass |

---

## Lighthouse Audit Results

| Metric         | Score |
| -------------- | ----- |
| Performance    | 78    |
| Accessibility  | 74    |
| Best Practices | 100   |
| SEO            | 42    |

### Performance Metrics

| Metric                         | Result |
| ------------------------------ | ------ |
| First Contentful Paint (FCP)   | 1.1 s  |
| Largest Contentful Paint (LCP) | 2.1 s  |
| Total Blocking Time (TBT)      | 0 ms   |
| Speed Index                    | 1.9 s  |
| Cumulative Layout Shift (CLS)  | 0.157  |

---

## JMeter Performance Testing

### Test Configuration

| Parameter      | Value  |
| -------------- | ------ |
| Users          | 50     |
| Loop Count     | 5      |
| Total Requests | 250    |
| Ramp-Up Time   | 10 sec |

### Aggregate Report

| Metric                | Result   |
| --------------------- | -------- |
| Average Response Time | 1785 ms  |
| Median                | 1414 ms  |
| Minimum               | 299 ms   |
| Maximum               | 8082 ms  |
| Error Rate            | 0.00%    |
| Throughput            | 21.0/sec |

### Summary Report

| Metric             | Result   |
| ------------------ | -------- |
| Total Samples      | 250      |
| Average            | 1785 ms  |
| Standard Deviation | 1375.50  |
| Throughput         | 21.0/sec |
| Received KB/sec    | 468.40   |
| Sent KB/sec        | 6.36     |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/AnjilaBohora/Demo_webapp_automation.git
cd Demo_webapp_automation
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running Tests

Execute all test cases:

```bash
pytest -v
```

Generate HTML Report:

```bash
pytest --html=reports/report.html
```

---

## Test Report

After execution, the HTML report can be found at:

```text
reports/report.html
```

---

## Performance Testing

### Lighthouse Recommendations

#### Performance

* Optimize images
* Enable lazy loading
* Minimize unused CSS and JavaScript
* Improve caching
* Use CDN

#### Accessibility

* Add ARIA labels
* Improve keyboard navigation
* Enhance color contrast
* Add meaningful alt text

#### SEO

* Improve metadata
* Use semantic HTML
* Optimize mobile experience
* Improve page titles and descriptions

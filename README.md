# 🕷️ Python Web Scraping — BeautifulSoup & Requests

A hands-on **Python web scraping project** exploring how websites can be fetched, parsed, navigated, and analyzed programmatically using **BeautifulSoup** and **Requests**.

The repository progresses from understanding basic HTML parsing to working with real-world web pages and extracting useful information from their HTML structure.

---

## 📌 About the Project

Web scraping is the process of programmatically retrieving and extracting information from websites.

This project was created to explore the complete basic scraping pipeline:

```text
Website / HTML
      ↓
HTTP Request
      ↓
Raw HTML
      ↓
BeautifulSoup Parser
      ↓
Navigate HTML Structure
      ↓
Find Tags & Attributes
      ↓
Extract Useful Data
```

The repository contains two main web-scraping exercises:

```text
Web Scraping 1
Web Scraping 2
```

Together, they cover both **local HTML parsing** and **real-world website scraping**.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **BeautifulSoup4** | HTML parsing and navigation |
| **Requests** | Retrieving web pages through HTTP |
| **HTML** | Structure being parsed and analyzed |
| **Jupyter / Python Environment** | Running and experimenting with scraping code |

---

# 📂 Repository Structure

```text
Python-Web-Scraping/
│
├── WebScrapping1
├── WebScrapping2
├── index.html
└── README.md
```

> File names may vary depending on whether the exercises are stored as Python scripts or notebooks.

---

# 🔍 Web Scraping 1 — HTML Parsing Fundamentals

The first part focuses on learning how **BeautifulSoup represents and navigates HTML documents**.

A local HTML file is opened using Python:

```python
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
```

This converts raw HTML into a structure that Python can navigate and manipulate.

---

## 🌳 Understanding the HTML Tree

HTML documents contain nested elements:

```html
<html>
    <head>
        <title>Example</title>
    </head>

    <body>
        <h1>Heading</h1>
        <p>Paragraph</p>
    </body>
</html>
```

BeautifulSoup parses this structure into a tree of Python objects.

Conceptually:

```text
HTML
 │
 ├── HEAD
 │    └── TITLE
 │
 └── BODY
      ├── H1
      ├── P
      └── A
```

This makes individual elements accessible programmatically.

---

# 🎨 Pretty Printing HTML

BeautifulSoup can format messy HTML into a more readable structure using:

```python
print(doc.prettify())
```

This is useful when inspecting unfamiliar pages because it exposes the hierarchy and nesting of the document.

---

# 🏷️ Accessing HTML Tags

Individual HTML elements can be retrieved directly.

For example:

```python
tag = doc.title
print(tag)
```

returns the `<title>` element.

The text inside the element can then be accessed using:

```python
print(tag.string)
```

This demonstrates the difference between:

```text
HTML Element
      ↓
<title>Example</title>

Text Content
      ↓
Example
```

---

# ✏️ Modifying HTML

BeautifulSoup can also modify the parsed document.

For example:

```python
tag.string = "hello"
```

changes the contents of the title element.

This demonstrates that BeautifulSoup is useful not only for extracting information but also for **manipulating parsed HTML structures**.

---

# 🔎 Finding Multiple Elements

Real websites frequently contain many elements with the same tag.

BeautifulSoup provides:

```python
find_all()
```

For example:

```python
tags = doc.find_all("p")
```

can retrieve paragraph elements.

Searches can also be nested.

```python
tags.find_all("b")
```

can be used to search for bold elements inside another selected HTML element.

Conceptually:

```text
Document
   │
   └── <p>
        │
        ├── <b>
        └── <b>
```

This is an important technique when extracting information from larger pages.

---

# 🌐 Web Scraping 2 — Scraping a Real Website

The second part moves beyond local HTML and works with a **real webpage**.

Python's `requests` library is used to retrieve the page:

```python
import requests

result = requests.get(url)
```

The returned HTML is then passed into BeautifulSoup:

```python
doc = BeautifulSoup(result.text, "html.parser")
```

This creates the fundamental web-scraping pipeline:

```text
URL
 │
 ▼
requests.get()
 │
 ▼
HTTP Response
 │
 ▼
response.text
 │
 ▼
BeautifulSoup
 │
 ▼
Parsed HTML
```

---

# 🛍️ Real-World E-Commerce Parsing

The project experiments with a real **e-commerce product page**.

Unlike the simple local HTML example, a production website contains a much larger document with:

- Product information
- Metadata
- Navigation
- Images
- Prices
- Categories
- JavaScript
- CSS references
- Analytics information
- Structured data
- Links
- Forms
- Attributes

This provides experience working with HTML that more closely resembles what a real scraper encounters.

---

# 📦 Discovering Product Data

One interesting part of scraping modern e-commerce websites is that useful information may appear in structured metadata.

For example, a page may contain information conceptually similar to:

```json
{
    "name": "Product Name",
    "category": "Shirts",
    "price": "2990.00"
}
```

The inspected product page contains product metadata including a product identifier, name, category and price.

This demonstrates an important scraping concept:

> Useful information is not always located in the visible text of a webpage. It may also exist inside metadata, attributes, scripts, or structured data.

---

# 🧾 Structured Data

Modern websites may expose machine-readable information using structured data such as:

```html
<script type="application/ld+json">
```

The page inspected in this project includes structured product information describing properties such as:

```text
Product Name
Description
SKU
Brand
Images
Price
Currency
Availability
```

This type of data can often be much easier to process than manually extracting information from deeply nested visual HTML.

---

# 🧠 Core Concepts Explored

## 1. HTTP Requests

Using:

```python
requests.get()
```

to retrieve HTML from a remote web server.

---

## 2. HTML Parsing

Using:

```python
BeautifulSoup(html, "html.parser")
```

to transform raw HTML into a navigable Python structure.

---

## 3. DOM Navigation

Understanding relationships between HTML elements and navigating through the parsed document.

---

## 4. Tag Extraction

Accessing specific elements such as:

```text
<title>
<p>
<b>
<a>
<h1>
<h2>
```

---

## 5. Multiple Element Searching

Using:

```python
find_all()
```

to locate multiple matching HTML elements.

---

## 6. Nested Searching

Searching inside previously selected elements to progressively narrow down the required information.

```text
Document
   ↓
Find Parent Element
   ↓
Search Inside Parent
   ↓
Find Child Elements
   ↓
Extract Data
```

---

## 7. HTML Manipulation

Changing the contents of parsed HTML elements through BeautifulSoup.

---

## 8. Real-World HTML Inspection

Working with large production HTML documents containing significantly more complexity than manually written example pages.

---

## 9. Structured Data

Recognizing machine-readable product information embedded within webpages.

---

# 🔄 Web Scraping Workflow

A typical scraper follows this architecture:

```text
                 ┌──────────────┐
                 │     URL      │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │   Requests   │
                 │  HTTP GET    │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │   Raw HTML   │
                 └──────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ BeautifulSoup │
                │    Parser     │
                └───────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ Search HTML  │
                 │ Tags / Data  │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ Extract Data │
                 └──────────────┘
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Install the required dependencies:

```bash
pip install beautifulsoup4 requests
```

If the project is stored as Jupyter notebooks, Jupyter can also be installed using:

```bash
pip install notebook
```

Then start it with:

```bash
jupyter notebook
```

---

# 📦 Dependencies

The main dependencies are:

```text
beautifulsoup4
requests
```

They can optionally be placed inside a `requirements.txt` file:

```text
beautifulsoup4
requests
```

and installed with:

```bash
pip install -r requirements.txt
```

---

# 💡 Example

A minimal example of the concepts explored in this repository:

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)
print(soup.title.string)

links = soup.find_all("a")

for link in links:
    print(link.get("href"))
```

The process is:

```text
Request Page
     ↓
Receive HTML
     ↓
Parse HTML
     ↓
Find Elements
     ↓
Extract Information
```

---

# 🛡️ Responsible Web Scraping

Web scraping should be performed responsibly.

Before building a scraper for a website:

- Review the website's Terms of Service.
- Respect applicable `robots.txt` guidance.
- Avoid sending excessive requests.
- Use reasonable delays for repeated scraping.
- Do not attempt to bypass authentication or access controls.
- Avoid collecting private or sensitive information.
- Prefer an official API when one is available and appropriate.

The examples in this repository are intended for **learning and experimentation with publicly accessible webpage content**.

---

# ⚠️ Limitations

This project focuses on the fundamentals of scraping and HTML parsing.

It does not currently implement:

- Large-scale crawling
- Browser automation
- JavaScript rendering
- Proxy rotation
- CAPTCHA handling
- Authentication
- Scraping databases
- Automatic pagination
- Production-scale retry handling

Websites can also change their HTML structure over time, meaning selectors written for a particular page may eventually need to be updated.

---

# 🔮 Possible Future Improvements

The project could be expanded with:

- 📊 Export scraped data to CSV
- 🐼 Analyze results using Pandas
- 🗄️ Store scraped data in a database
- 🔄 Automatically scrape multiple pages
- 📑 Pagination support
- 🖼️ Extract product image URLs
- 💰 Product price tracking
- 🔔 Price-change notifications
- 📈 Historical price analysis
- 🧹 Automated data cleaning
- 📝 JSON export
- ⏱️ Request throttling
- 🧪 Error handling and retries
- 🌐 Selenium or Playwright for JavaScript-heavy websites

---

# 🎯 Project Purpose

The purpose of this repository is to develop a practical understanding of how information available on the web can be retrieved and processed programmatically.

It demonstrates the progression from:

```text
Understanding HTML
        ↓
Parsing Local HTML
        ↓
Navigating Tags
        ↓
Finding Elements
        ↓
Sending HTTP Requests
        ↓
Parsing Real Websites
        ↓
Extracting Structured Information
```

Rather than treating web scraping as simply copying information from a webpage, the project explores the underlying relationship between **HTTP, HTML structure, parsing, and data extraction**.

---

# 📚 What I Learned

Through these exercises, I gained hands-on experience with:

- Python web scraping
- BeautifulSoup
- Requests
- HTTP responses
- HTML structure
- DOM-style navigation
- HTML tags and attributes
- `find()` and `find_all()`
- Nested element searching
- Parsing local HTML files
- Fetching remote webpages
- Inspecting real-world HTML
- E-commerce webpage structure
- Structured web data
- Basic data extraction techniques

---

# 📌 Summary

This repository documents my introduction to **web scraping with Python**, progressing from basic HTML parsing to retrieving and analyzing real-world webpages.

The core workflow can be summarized as:

```text
        Python
          │
          ▼
       Requests
          │
          ▼
      Web Server
          │
          ▼
       Raw HTML
          │
          ▼
    BeautifulSoup
          │
          ▼
     Parsed Data
          │
          ▼
  Useful Information
```

The project provides a foundation for more advanced work in **data extraction, automation, data engineering, analytics, and web-based data collection**.

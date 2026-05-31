# Flipkart Mobile App Scraper

This project automates Flipkart Android mobile app scraping using:

- Python
- Appium
- Pytest
- POM Design Pattern
- MySQL
- OpenPyXL

## Features

- Category Page Scraping
- Product Detail Page Scraping
- Product Highlights Extraction
- Specifications Extraction
- Description Extraction
- MySQL Storage
- XLS Output Generation

## Run Project

```
pytest
```


## Tech Stack

```
Python
Appium
Pytest
MySQL
OpenPyXL
```

---

# STEP 6 — CREATE GITHUB REPOSITORY

Go to:

```text
https://github.com


Click : 
New Repository

Repository Name :
flipkart-mobile-scraper

Set : 
Public

Click : 
Create Repository
```


# STEP 7 — PUSH PROJECT TO GITHUB

```
Open PyCharm Terminal : 

git init
git add .
git commit -m "Initial Flipkart mobile scraper project"

Add GitHub remote:
git remote add origin YOUR_GITHUB_REPO_LINK

Push code:
git branch -M main
git push -u origin main
```

# STEP 8 — VERIFY OUTPUT FILE

```
After running pytest:

output/products.xlsx

should be generated.
Commit and push that XLS file also to GitHub.


# PMP_Playwright

Setup Check (Python + Pytest)
pip install playwright pytest
playwright install

---------------------

Install Playwright (Hands-On)
Create a new empty folder:

mkdir playwright-basics
cd playwright-basics

---------------------

Run:

npm init playwright@latest

---------------------

Select these options (IMPORTANT):

✔️ TypeScript → YES

✔️ Tests folder → YES

✔️ GitHub Actions → YES

✔️ Install Playwright browsers → YES

-----------------------------------------

Locator Hierarchy (Use This Order)

This is Playwright best practice. Memorize it.

get_by_role() ✅ (BEST)

get_by_label()

get_by_test_id()

CSS selectors

XPath ❌ (last resort only)
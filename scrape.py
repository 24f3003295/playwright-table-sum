from playwright.sync_api import sync_playwright

urls = [
"https://sanand0.github.io/tdsdata/js_table/?seed=76",
"https://sanand0.github.io/tdsdata/js_table/?seed=77",
"https://sanand0.github.io/tdsdata/js_table/?seed=78",
"https://sanand0.github.io/tdsdata/js_table/?seed=79",
"https://sanand0.github.io/tdsdata/js_table/?seed=80",
"https://sanand0.github.io/tdsdata/js_table/?seed=81",
"https://sanand0.github.io/tdsdata/js_table/?seed=82",
"https://sanand0.github.io/tdsdata/js_table/?seed=83",
"https://sanand0.github.io/tdsdata/js_table/?seed=84",
"https://sanand0.github.io/tdsdata/js_table/?seed=85"
]

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for url in urls:
        page.goto(url)
        page.wait_for_selector("table")

        cells = page.query_selector_all("td")

        for cell in cells:
            text = cell.inner_text()
            try:
                total_sum += int(text)
            except:
                pass

    browser.close()

print("FINAL TOTAL =", total_sum)

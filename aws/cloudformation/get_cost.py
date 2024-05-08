from playwright.sync_api import sync_playwright
import subprocess

# Define the AWS CLI command as a list of arguments
aws_cli_command = [
    "aws",
    "cloudformation",
    "estimate-template-cost",
    "--template-body", "file://cloudformation.yaml",
    "--region", "us-east-1",
    "--output", "json",
    "--query", "Url"
]

# Run the AWS CLI command and capture the output
print("Getting pricing url...")
result = subprocess.run(aws_cli_command, capture_output=True, text=True)

# Check if the command executed successfully
if result.returncode == 0:
    # Get the command's output
    url = result.stdout.strip().strip('"')  # Strip any leading or trailing whitespace
    # Print the URL
    print(url)

# CSS selector for the elements you want to query
    css_selector = "div.price-banner-amount-bold"

    # Start Playwright and create a browser instance
    with sync_playwright() as p:
        # Launch a Chromium browser (set headless=False if you want to see the browser)
        print("Opening browser...")
        browser = p.chromium.launch(headless=True)

        # Create a new page
        page = browser.new_page()

        print("Navigating to the URL...")
        page.goto(url)

        # Allow some time for JavaScript to execute and page to load
        page.wait_for_timeout(10000)  # Adjust the timeout as needed

        # Use page.query_selector_all() to find all elements matching the CSS selector
        elements = page.query_selector_all(css_selector)

        # Iterate through the elements and print their text content
        for element in elements:
            # Get the text content of the element
            text_content = element.inner_text()

            # Print the text content
            print(f"Cost estimation is: {text_content}")

        # Close the browser
        browser.close()

else:
    # If the command failed, print the error message
    print(f"Error executing command: {result.stderr}")

# Website Availability Checker
# pip install requests

import requests


def check_website(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        print("\n===== WEBSITE STATUS =====")
        print("Website:", url)
        print("Final URL:", response.url)
        print("HTTP Status:", response.status_code)

        if response.ok:
            print("Result: Website responded successfully.")
        else:
            print("Result: Website returned an HTTP error.")

    except requests.RequestException as error:
        print("Unable to reach website:", error)


website = input("Enter website URL: ").strip()

if website:
    check_website(website)
else:
    print("Website URL cannot be empty.")
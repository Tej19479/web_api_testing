import os
from datetime import datetime
from pytest_check import check
import pytest_html  # pip install pytest-html

def save_step_screenshot(driver, test_name):
    today = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%H-%M-%S")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_dir = os.path.join("reports", "assertion_screenshot", today)
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)
    driver.save_screenshot(screenshot_path)
    return screenshot_path


def soft_check(driver, condition, message, test_name, request_node):
    screenshot_path = save_step_screenshot(driver, test_name)
    print("soft check image path",screenshot_path)
    html_block = f"""
        <div style="border:1px solid {'green' if condition else 'red'}; padding:10px; margin:10px;">
            <p><strong>Soft Assertion {'Passed ✅' if condition else 'Failed ❌'}:</strong> {message}</p>
            <p><a href="{os.path.abspath(screenshot_path)}" target="_blank">📷 View Screenshot</a></p>
            <p color:red> TEJ PRTAP SIGH</p>
            <img src="{os.path.abspath(screenshot_path)}" alt="screenshot" style="max-width:400px;" />
        </div>
    """

    # Add a custom section label: "Assertion Logs"
    assertion_log = pytest_html.extras.html(f"""
        <details open>
            <summary><strong>{test_name} - Assertion Log</strong></summary>
            {html_block}
        </details>
    """)

    if not hasattr(request_node, "assertion_logs"):
        request_node.assertion_logs = []

    request_node.assertion_logs.append(assertion_log)

    check.is_true(condition, message)
import time
# import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import yaml
import pytest_html
from chromedriver_py import binary_path

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from py.xml import html  # Required to format HTML
import base64

@pytest.fixture(scope='session')
def config():
    with open("utils/config.yaml", 'r') as f:
        data = yaml.safe_load(f)
        print("data in yaml file",data)
    return data
@pytest.fixture
def driver():

    options=webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    # options.add_argument("--disable-extensions")
    # driver = webdriver.Chrome(service=Service(executable_path=binary_path), options=options)
    chrome_driver_path = r"C:\Users\Tej\.wdm\drivers\chromedriver\win64\139.0.7258.68\chromedriver-win32\chromedriver.exe"
    service = Service(chrome_driver_path)
    driver=webdriver.Chrome(service=service,options=options)
    #driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

    driver.quit()

@pytest.fixture(scope='session')
def base_url(config):
        return config['app']['base_url']

@pytest.fixture(scope='session')
def base_app_login_url(config):
    return config['app']['login_url']

#     # Define custom log level: SPAM
# SPAM = 5
# logging.addLevelName(SPAM, "SPAM")
#
# def spam(self, message, *args, **kwargs):
#         if self.isEnabledFor(SPAM):
#             self._log(SPAM, message, args, **kwargs)
#
# logging.Logger.spam = spam
#
# @pytest.hookimpl(trylast=True)
# def pytest_configure(config):
#         logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
#
#         # Change color for standard level
#         logging_plugin.log_cli_handler.formatter.add_color_level(logging.INFO, "cyan")
#
#         # Add color for custom level SPAM
#         logging_plugin.log_cli_handler.formatter.add_color_level(SPAM, "blue")


#



#report  code gernate



# conftest.py

#
# def get_screenshot_path(test_name, status):
#     today = datetime.now().strftime("%Y-%m-%d")
#     time_stamp = datetime.now().strftime("%H-%M-%S")
#     folder = os.path.join("reports", today, "screenshots")
#     os.makedirs(folder, exist_ok=True)
#     filename = f"{status.upper()}_{test_name}_{time_stamp}.png"
#     return os.path.join(folder, filename)
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Attach screenshots to pytest-html report for both pass and fail"""
#     outcome = yield
#     rep = outcome.get_result()
#     driver = item.funcargs.get("driver", None)
#     test_name = item.name
#     extra = getattr(rep, "extra", [])
#     if rep.when == "call" and driver:
#         status = "pass" if rep.passed else "fail"
#         screenshot_path = get_screenshot_path(test_name, status)
#         print("screenshot path",screenshot_path)
#         try:
#             driver.save_screenshot(screenshot_path)
#
#             # Attach screenshot to report
#             if os.path.exists(screenshot_path):
#                 with open(screenshot_path, "rb") as image_file:
#                     encoded_image = base64.b64encode(image_file.read()).decode()
#
#                 extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
#                 extra.append(pytest_html.extras.image(screenshot_path))
#                 extra.append(pytest_html.extras.image(encoded_image, mime_type="image/png"))
#
#
#                 rep.extra = extra
#         except Exception as e:
#             print(f"Error saving or attaching screenshot: {e}")
#
#





import os
import base64
from datetime import datetime
import pytest

pytest_html = None

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")

def get_screenshot_path(test_name, status):
    today = datetime.now().strftime("%Y-%m-%d")
    time_stamp = datetime.now().strftime("%H-%M-%S")
    folder = os.path.join("reports", today, "screenshots")
    print("folder locaion of screenshot",folder)
    os.makedirs(folder, exist_ok=True)
    filename = f"{status.upper()}_{test_name}_{time_stamp}.png"
    full_path = os.path.join(folder, filename)
    print("full path of the loction of",full_path)
    relative_path = os.path.join("screenshots", filename)
    print(os.path,"ddddddd",relative_path)

    return os.path.join(folder, filename),relative_path,full_path

# def pytest_configure(config):
#     if not config.option.html
#
# def pytest_addoption(parser):
#
#     today = datetime.now().strftime("%Y-%m-%d")
#     report_dir = os.path.join("reports", today)
#     os.makedirs(report_dir, exist_ok=True)
#     timestamp = datetime.now().strftime("%H-%M-%S")
#     report_file = f"report_{timestamp}.html"
#     default_html = os.path.join(report_dir, "report.html")
#     config.option.html = default_html
#
#     # parser.addoption(
#     #     "--html", action="store", default=default_html, help="HTML report path"
#     # )

# def pytest_configure(config):
#     if not hasattr(config.option, "htmlpath") or config.option.htmlpath is None:
#         # Generate date & time-based folder and filename
#         today = datetime.now().strftime("%Y-%m-%d")
#         timestamp = datetime.now().strftime("%H-%M-%S")
#         report_dir = os.path.join("reports", today)
#         os.makedirs(report_dir, exist_ok=True)
#
#         # Final report path
#         report_file = f"report_{timestamp}.html"
#         report_path = os.path.join(report_dir, report_file)
#         config.option.htmlpath = report_path
#     config.option.self_contained_html = True
# # def pytest_addoption(parser):
# #     group = parser.getgroup("terminal reporting")
# #     group.addoption(
# #         "--self-contained-html",
# #         action="store_true",
# #         help="Embed assets into the HTML report",
# #         default=True  # Ensures it's enabled by default
# #     )


# def pytest_cmdline_preparse(config, args):
#     if "--self-contained-html" not in args:
#         args.append("--self-contained-html")



#new code aaddddddddddddddddddddddddddddddd

import os
from datetime import datetime
import pytest

def get_timestamp():
    return datetime.now().strftime("%H-%M-%S")

def save_step_screenshot(driver, test_name, step_name, item):
    folder = os.path.join("reports", "step_screenshots", test_name)
    os.makedirs(folder, exist_ok=True)
    filename = f"{step_name}_{get_timestamp()}.png"
    path = os.path.join(folder, filename)
    driver.save_screenshot(path)
   # print(f"[Screenshot] Step: {step_name}, Path: {path}")

    # Store screenshot paths in item for later report use
    if not hasattr(item, "step_screenshots"):
        item.step_screenshots = []
    item.step_screenshots.append(path)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    print("rep                jjjj",rep)
    extras = getattr(rep, "extras", [])
    #print("extras                jjjj", extras)
    if rep.when == "call":
        driver = item.funcargs.get("driver", None)
        if driver:
            # Determine status: passed, failed, xfail, xpassed, etc.
            xfail = hasattr(rep, "wasxfail")
            if rep.passed:
                status = "xpassed" if xfail else "passed"
            elif rep.failed:
                status = "xfail" if xfail else "failed"
            else:
                status = "unknown"

            # Capture screenshot
            test_name = item.name
            screenshot_path,relative_path ,full_path= get_screenshot_path(test_name, status)
            try:
                driver.save_screenshot(screenshot_path)
               # print(f"Screenshot saved at: {screenshot_path}")
                screenshot_image=os.path.join(os.getcwd(),full_path.lstrip("\\"))
                #extras.append(pytest_html.extras.image(screenshot_path))
              #  print("screenshot_image",screenshot_image)
                page_title = driver.title if driver.title else "No Title"
                html_t= html_t = f'''
                <div>
                <div style="border:1px solid #ccc; padding:10px; margin:10px 0;">
                    <p><strong>Test Name:</strong> {test_name}</p>
                    <p><strong>Status:</strong> {status.upper()}</p>
                    <p><strong>Page Title:</strong> {page_title}</p>
                    <img src="{screenshot_image}" alt="screenshot" style="width:304px;height:228px;"
                         onclick="window.open(this.src)" align="right"/>
                         <p>this runing test case image {test_name} </p>
                        <p><a href="{screenshot_image}" target="_blank">📸 View Full Screenshot</a></p>
                '''
                extras.append(pytest_html.extras.html(html_t))
                rep.extras = extras
                #new line adddd
                if hasattr(item, "step_screenshots"):
                    print("📦 item.step_screenshots =", item.step_screenshots)
                    step_html = "<details><summary><strong>📷 Step-wise Assertions</strong></summary>"
                    for step_path in item.step_screenshots:
                        html_step = f"""
                                        <div style="margin:5px 0;padding:5px;border:1px dashed #999;">
                                            <p>Step Screenshot:{page_title} ---{test_name}</p>
                                            <img src="{os.path.abspath(step_path)}" width="300"/>
                                            <p><a href="{os.path.abspath(step_path)}" target="_blank">🔍 Full View</a></p>
                                        </div>
                                        """
                        extras.append(pytest_html.extras.html(html_step))
                        extras.append(pytest_html.extras.html(step_html))
                #hdhhdhdh
                if hasattr(item, "assertion_logs"):
                    for log in item.assertion_logs:
                        extras.append(log)

                rep.extras = extras
            except Exception as e:
                print(f"Error capturing screenshot: {e}")

# # run_tests.py
# import os
# from datetime import datetime
# import subprocess
#
# # Create folder with today's date
# today = datetime.now().strftime("%Y-%m-%d")
# report_dir = os.path.join("reports", today)
# os.makedirs(report_dir, exist_ok=True)
#
# # Unique HTML file name with timestamp
# timestamp = datetime.now().strftime("%H-%M-%S")
# report_file = os.path.join(report_dir, f"Test_Report_{timestamp}.html")
#
# # Run pytest with html report output
# subprocess.run([
#     "pytest",
#     "--html=" + report_file,
#     "--self-contained-html",
#     "--capture=tee-sys"  # To also show print statements
# ]           )

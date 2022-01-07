rem chrome
pytest -v -s -m "sanity" --html=./Reports/report_chrome.html TestCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/report.html TestCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html TestCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html TestCases/ --browser chrome

rem firefox
rem pytest -s -v -m "sanity" --html=./Reports/report_firefox.html TestCases/ --browser firefox
rem pytest -s -v -m "regression" --html=./Reports/report.html TestCases/ --browser firefox
rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html TestCases/ --browser firefox
rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html TestCases/ --browser firefox
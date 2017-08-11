# weather-report-current-conditions

Extracts data from Weather Underground's https://www.wunderground.com/weather/api/ API and prints to screen.

I run it on one of my Raspberry Pi using cron, it is then emailed to me on a three hourly basis, with a command similar to this:

0 */3 * * * cd /file/location/ && python weather-report-current-conditions.py | mail -s Subject_of_Mail myemail@address.com

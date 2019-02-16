import json, requests

# TODO: Automate function to get all

def getSearchResponse():
    url = "https://sprs.parl.gov.sg/search/searchResult"
    querystring = {"":""}

    payload = "{\n    \"keyword\": \"undefined\",\n    \"fromday\": \"16\",\n    \"frommonth\": \"02\",\n    \"fromyear\": \"2019\",\n    \"today\": \"16\",\n    \"tomonth\": \"02\",\n    \"toyear\": \"2019\",\n    \"dateRange\": \"* TO NOW\",\n    \"reportContent\": \"with all the words\",\n    \"parliamentNo\": \"\",\n    \"selectedSort\": \"date_dt desc\",\n    \"portfolio\": \"undefined\",\n    \"mpName\": \"\",\n    \"rsSelected\": \"\",\n    \"lang\": \"\",\n    \"startIndex\": \"0\",\n    \"endIndex\": \"19\",\n    \"titleChecked\": \"false\",\n    \"ministrySelected\": \"\"\n}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "0a18881c-ae1b-4b23-80d2-a62426a118b1"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    return response

searchResponse = getSearchResponse() 

def generateReportUrl(reportId):
    return "https://sprs.parl.gov.sg/search/sprs3topic?reportid=" + reportId

def getReportIds(jsonObject):
    reportIds = []
    for entry in jsonObject:
        reportIds.append(entry["reportId"])
    return reportIds

for reportId in getReportIds(searchResponse.json()):
    urls = []
    urls.append(generateReportUrl(reportId))

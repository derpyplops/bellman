import json, requests

# TODO: Automate function to get all

def getSearchResponse(startIndex):
    endIndex = startIndex + 19
    url = "https://sprs.parl.gov.sg/search/searchResult"
    querystring = {"":""}

    # payload = "{\n    \"keyword\": \"undefined\",\n    \"fromday\": \"16\",\n    \"frommonth\": \"02\",\n    \"fromyear\": \"2019\",\n    \"today\": \"16\",\n    \"tomonth\": \"02\",\n    \"toyear\": \"2019\",\n    \"dateRange\": \"* TO NOW\",\n    \"reportContent\": \"with all the words\",\n    \"parliamentNo\": \"\",\n    \"selectedSort\": \"date_dt desc\",\n    \"portfolio\": \"undefined\",\n    \"mpName\": \"\",\n    \"rsSelected\": \"\",\n    \"lang\": \"\",\n    \"" + str(startIndex) +"\": \"0\",\n    \"endIndex\": " + str(endIndex) +",\n    \"titleChecked\": \"false\",\n    \"ministrySelected\": \"\"\n}"
    payload = {  
    "keyword":"undefined",
    "fromday":"17",
    "frommonth":"02",
    "fromyear":"2019",
    "today":"17",
    "tomonth":"02",
    "toyear":"2019",
    "dateRange":"* TO NOW",
    "reportContent":"with all the words",
    "parliamentNo":"",
    "selectedSort":"date_dt desc",
    "portfolio":"undefined",
    "mpName":"",
    "rsSelected":"",
    "lang":"",
    "startIndex": str(startIndex),
    "endIndex":str(endIndex),
    "titleChecked":"false",
    "ministrySelected":""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "0a18881c-ae1b-4b23-80d2-a62426a118b1"
        }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, params=querystring)
    return response

def getOralResponse(startIndex):
    endIndex = startIndex + 19
    url = "https://sprs.parl.gov.sg/search/searchResult"
    querystring = {"":""}

    # payload = "{\n    \"keyword\": \"undefined\",\n    \"fromday\": \"16\",\n    \"frommonth\": \"02\",\n    \"fromyear\": \"2019\",\n    \"today\": \"16\",\n    \"tomonth\": \"02\",\n    \"toyear\": \"2019\",\n    \"dateRange\": \"* TO NOW\",\n    \"reportContent\": \"with all the words\",\n    \"parliamentNo\": \"\",\n    \"selectedSort\": \"date_dt desc\",\n    \"portfolio\": \"undefined\",\n    \"mpName\": \"\",\n    \"rsSelected\": \"\",\n    \"lang\": \"\",\n    \"" + str(startIndex) +"\": \"0\",\n    \"endIndex\": " + str(endIndex) +",\n    \"titleChecked\": \"false\",\n    \"ministrySelected\": \"\"\n}"
    payload = {  
    "keyword":"undefined",
    "fromday":"17",
    "frommonth":"02",
    "fromyear":"2019",
    "today":"17",
    "tomonth":"02",
    "toyear":"2019",
    "dateRange":"* TO NOW",
    "reportContent":"with all the words",
    "parliamentNo":"",
    "selectedSort":"date_dt desc",
    "portfolio":"undefined",
    "mpName":"",
    "rsSelected":"oral-answer",
    "lang":"",
    "startIndex": str(startIndex),
    "endIndex": str(endIndex),
    "titleChecked":"false",
    "ministrySelected":""
    }

    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "0a18881c-ae1b-4b23-80d2-a62426a118b1"
        }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, params=querystring)
    return response

def getTextResponse(reportId):
    url = "https://sprs.parl.gov.sg/search/getHansardTopic/"

    querystring = {"":"","id":reportId}

    payload = "{method: null, headers: {Content-Type: [\"application/json\"]}, body: null, url: null}\r\nbody: null\r\nheaders: {Content-Type: [\"application/json\"]}\r\nContent-Type: [\"application/json\"]\r\n0: \"application/json\"\r\nmethod: null\r\nresponseType: null\r\nurl: null\r\nwithCredentials: null"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "99436b1b-e33f-4dd1-aa40-a4051d013406"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    return response

# last one 6760
searchStartIndex = 0
searchResponse = getOralResponse(searchStartIndex)

def generateReportUrl(reportId):
    return "https://sprs.parl.gov.sg/search/sprs3topic?reportid=" + reportId

def getReportIds(jsonObject):
    reportIds = []
    for entry in jsonObject:
        reportIds.append(entry["reportId"])
    return reportIds

urls = []
names = []
counter = searchStartIndex
resultHTML = None

while searchStartIndex < 28777:
    for reportId in getReportIds(searchResponse.json()):
        print(reportId[0:11])
        # if reportId[0:11] == "oral-answer":
        # try:
        response = getTextResponse(reportId[:-1])
        if "resultHTML" in response:
            resultHTML = response.json()["resultHTML"]
        elif "htmlContent" in response:
            resultHTML = response.json()["htmlContent"]
        else:
            print("Error.")
        
        with open("jsons/"+ reportId[:-1] + ".json", 'w') as outfile:
            json.dump(resultHTML, outfile)
            print("Created:[{}] ".format(str(counter)) + reportId)
        # except:
        #     print("Error: " + reportId)
        counter += 1
    searchStartIndex += 20
    searchResponse = getOralResponse(searchStartIndex)

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
URL = "https://cdn3.digialm.com//per/g28/pub/2083/touchstone/AssessmentQPHTMLMode1//2083O23190/2083O23190S8D691/16877878040924186/DL01065342_2083O23190S8D691E6.html"
URL2 = "https://cdn3.digialm.com//per/g28/pub/2083/touchstone/AssessmentQPHTMLMode1//2083O23190/2083O23190S8D2327/16877876593772681/DL01043819_2083O23190S8D2327E1.html"
def find_11_digit_numbers(text):
    pattern = r"\b\d{10,11}\b"
    matches = re.findall(pattern, text)
    return matches
URL3 = 'https://cdn3.digialm.com//per/g28/pub/2083/touchstone/AssessmentQPHTMLMode1//2083O23227/2083O23227S35D408/16877923744464249/DL01043819_2083O23227S35D408E2.html'

def getmarks(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser")
    questions = soup.find_all('table',class_='menu-tbl')
    option_selected = []
    for question in questions:
        options = question.findAll('td')
        question_response = []
        for option in options:
            findkey = find_11_digit_numbers(str(option))
            if findkey != []:
                question_response.append(findkey[0])
        if(options[-1].text.strip() == '--'):
            continue
        response_selected = question_response[int(options[-1].text.strip())]
        diction = [int(question_response[0]), int(response_selected)]
        option_selected.append(diction)

    df = pd.read_excel(r'C:\Users\sagar\PycharmProjects\bot\answer.xlsx', sheet_name='Sheet4')
    df2 = pd.DataFrame(option_selected, columns=['Question', 'Correct Answer'])
    print(df.columns)
    print(df.head())
    print(df2.head())
    merge = pd.merge(df, df2, on='Question')
    count = 0
    total_correct = 0
    total_incorrect = -1
    for i in range(len(merge)):
        if merge['Answer'][i] == merge['Correct Answer'][i]:
            count += 4
            total_correct += 1
        else:
            total_incorrect += 1
            count += -1
    print(count)
    print(total_correct)
    print(total_incorrect)

print(getmarks(URL2))


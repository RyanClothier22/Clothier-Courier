import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def get_emails_on_list():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1U94k_4fzX6S7WxcxSRIkHYA0ZAZqoPNcq8E0KeK-DeM/edit?usp=sharing')
    worksheetName = "sheet1"
    worksheet = spreadsheet.worksheet(worksheetName)
    df = pd.DataFrame(worksheet.get_all_records())

    mailing_list_all = df['Email:'].to_list()
    mailing_list = []
    [mailing_list.append(x) for x in mailing_list_all if x not in mailing_list]

    return mailing_list



def remove_these_from_list():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1QM05Ah7V7WrBHNN8BAf9LUPvT-q37drXTFWXyojZE0o/edit?usp=sharing')
    worksheetName = "sheet1"
    worksheet = spreadsheet.worksheet(worksheetName)
    df = pd.DataFrame(worksheet.get_all_records())

    mailing_list_all = df['Email'].to_list()
    mailing_list = []
    [mailing_list.append(x) for x in mailing_list_all if x not in mailing_list]

    return  mailing_list


def get_emails():
    on = get_emails_on_list()
    off = remove_these_from_list()
    return [i for i in on if i not in off and len(i) > 7]

if __name__ == "__main__":
    print(get_emails())
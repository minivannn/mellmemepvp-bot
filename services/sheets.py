import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_CREDENTIALS_JSON, SHEET_ID

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(GOOGLE_CREDENTIALS_JSON, scope)
client = gspread.authorize(credentials)
sheet = client.open_by_key(SHEET_ID).sheet1

def record_vote(user_id, vote):
    sheet.append_row([str(user_id), str(vote)])

def get_leaderboard():
    rows = sheet.get_all_values()[1:]  # пропускаем заголовок
    scores = {}
    for row in rows:
        uid, vote = row
        scores[uid] = scores.get(uid, 0) + 1
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:10]

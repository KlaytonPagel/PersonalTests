#!/home/kpagel/Documents/drive_sync/bin/python3

import os.path
import io

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]


def check_token() -> str:
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds

def get_children(service, fileId, path='Saved_Files/') -> []:
    results = (
        service.files()
        .list(q=f"parents = '{fileId}'")
        .execute()
    )
    for child in results.get('files', []):
        if child['mimeType'] == "application/vnd.google-apps.folder":
            get_children(service, child['id'], f"{path}{child['name']}/")
        else:
            print(f"{path}{child['name']}")
            if not os.path.exists(path):
                os.makedirs(path)
            download_item(service, child['id'], f"{path}{child['name']}")

def download_item(service, fileId, path) -> None:
    request = (service.files().get_media(fileId=fileId))

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False

    while not done:
        status, done = downloader.next_chunk()
        print("%", end='')

    fh.seek(0)

    with open(path, 'wb') as file:
        file.write(fh.read())
        file.close()

def main():
    creds = check_token()
    try:
        service = build("drive", "v3", credentials=creds)

        # Call the Drive v3 API
        results = (
            service.files()
            .list(q="name = 'Saved_Files'")
            .execute()
        )
        root_folder_id = results.get("files", [])[0]['id']
        get_children(service, root_folder_id)
    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()

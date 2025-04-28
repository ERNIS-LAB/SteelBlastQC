import requests
import zipfile
import io


def download_and_extract_zip(extract_to: str):
    """
    Download a zip file from a DATAVERSE and extract its contents to a specified directory.
    If the specified directory does not exist, it will be created.

    Args:
        extract_to (str): The directory to extract the contents of the zip file to.
    """
    dataverse_url = "https://dataverse.nl/api/access/dataset/:persistentId/?persistentId=doi:10.34894/EKZNN0"

    response = requests.get(dataverse_url)

    if response.status_code == 200:
        if 'application/zip' not in response.headers.get('Content-Type', ''):
            print("The downloaded file is not a zip file.")
            print("Please try to download the file manually from the Dataverse.")
            print("See the ReadMe for more information.")
            return
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall(extract_to)
            print(f"Extracted files to: {extract_to}")

    else:
        print(f"Failed to download file: {response.status_code}")
        print("Please try to download the file manually from the Dataverse.")
        print("See the ReadMe for more information.")

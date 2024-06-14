import requests

BACKEND_URL = "http://localhost:8000/summary"

def get_summary(files):
    try:
        print(f"file name: {files[0].name}")
        print(f"file type: {files[0].type}")
        print(f"file value: {files[0].getvalue()[:100]}")

        files_to_send = [(file.name, file.getvalue(), file.type) for file in files]
        files = [('files', (name, value, type)) for name, value, type in files_to_send]

        # Envoyer la requête POST
        response = requests.post(BACKEND_URL, files=files)

        response.raise_for_status()
        print("Response status code:", response.status_code)
        print("Response JSON:", response.json())

        return response.json().get('summary', 'No summary found.')
    except requests.RequestException as e:
        # Imprimer l'erreur en détail
        print("Request failed:", e)
        if e.response is not None:
            print("Response status code:", e.response.status_code)
            print("Response content:", e.response.content)
        return f"Error: {e}"

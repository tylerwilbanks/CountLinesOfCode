import json

def _get_github_credentials() -> (str, str):
	access_token = None
	account_name = None
	with open("config.json", "r") as f:
		data = json.load(f)
		access_token = data["github_access_token"]
		account_name = data["github_account_name"]
	return access_token, account_name

REPOS_URL = "https://api.github.com/user/repos"
PERSONAL_ACCESS_TOKEN, ACCOUNT_NAME = _get_github_credentials()
REPOS_DIRECTORY = ".repos"
SUPPORTED_FILE_EXTENSIONS = [
	".kt",
	".py",
	".gd",
	".java",
	".html",
	".css",
	".javascript",
	".cs",
	".dart"
]
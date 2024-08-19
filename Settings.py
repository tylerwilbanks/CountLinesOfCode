import json

def _get_personal_access_token() -> str:
	access_token = None
	with open("config.json", "r") as f:
		data = json.load(f)
		access_token = data["github_access_token"]
	return access_token

REPOS_URL = "https://api.github.com/user/repos"
PERSONAL_ACCESS_TOKEN = _get_personal_access_token()
ACCOUNT_NAME = "tylerwilbanks"
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
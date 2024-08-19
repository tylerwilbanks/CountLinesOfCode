import json
import shutil
import requests
import Settings
from Repo import Repo
from Util import print_separator


class ProjectContainer:
	def __init__(self):
		self.repo_info_file_name = "RepoInfo.json"
		self.repos = []

	def clone_repos(self):
		headers = {
			"Authorization": f"token {Settings.PERSONAL_ACCESS_TOKEN}",
			"Accept": "application/vnd.github.v3+json"
		}

		params = {
			"visibility": "all",
			"per_page": 100
		}

		response = requests.get(Settings.REPOS_URL, headers=headers, params=params)
		with open(self.repo_info_file_name, "w") as f:
			json.dump(response.json(), f, indent=4)

		repos = response.json()

		for repo_json in repos:
			if not repo_json["owner"]["login"] == Settings.ACCOUNT_NAME:
				continue
			repo = Repo(Settings.REPOS_DIRECTORY, repo_json)
			repo.clone()


	def create_repos(self):
		with open(self.repo_info_file_name, "r") as f:
			data = json.load(f)
			for repo_json in data:
				if not repo_json["owner"]["login"] == Settings.ACCOUNT_NAME:
					continue
				repo = Repo(Settings.REPOS_DIRECTORY, repo_json)
				self.repos.append(repo)

	def process_repos(self):
		for repo in self.repos:
			repo.count_lines_in_directory()

	def display_info(self):
		self._display_summary()
		self._display_repo_info()

	def _display_summary(self):
		total_lines_across_all_projects = sum(repo.total_lines for repo in self.repos)
		print(f"Line Count Across All Projects: {total_lines_across_all_projects:,}")

	def _display_repo_info(self):
		for index, repo in enumerate(self.repos):
			print_separator()
			repo.display_info()
			if index + 1 == len(self.repos):
				print_separator()

	def clear_repos_folder(self):
		try:
			shutil.rmtree(Settings.REPOS_DIRECTORY)
		except Exception as e:
			print(f"failed to clean up directory: {Settings.REPOS_DIRECTORY} because: {e}")
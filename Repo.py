import glob
import os
import subprocess

import Settings


def count_lines_in_file(file_path) -> int:
	with open(file_path, 'r') as file:
		return sum(1 for line in file)


class Repo:
	def __init__(self, repos_directory, repo_json):
		self.name: str = str(repo_json["name"])
		self.json = repo_json
		self.directory: str = os.path.join(repos_directory, self.name)
		self.info = []
		self.total_lines = 0

	def clone(self):
		repo_url = self.json["clone_url"]
		if not os.path.exists(self.directory):
			os.makedirs(self.directory)
			subprocess.run(["git", "clone", repo_url, self.directory])
			print(f"Cloned {self.name}")
		else:
			print(f"{self.name} already exists")

	def count_lines_in_directory(self) -> int:
		for ext in Settings.SUPPORTED_FILE_EXTENSIONS:
			line_count_info = LineCountInfo(ext)
			for file_path in glob.glob(os.path.join(self.directory, '**', f'*{ext}') , recursive=True):
				line_count = count_lines_in_file(file_path)
				self.total_lines += line_count
				line_count_info.add_lines(line_count)
			if line_count_info.line_count > 0:
				self.info.append(line_count_info)
		return self.total_lines

	def display_info(self):
		print(f"{self.name}: Total Lines of Code: {self.total_lines:,}")


class LineCountInfo:
	def __init__(self, file_extension: str):
		self.file_type: str = file_extension
		self.line_count = 0

	def add_lines(self, line_count: int):
		self.line_count += line_count
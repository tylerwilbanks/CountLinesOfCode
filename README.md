# CountLinesOfCode
💻 Counts all the lines of code across all of your github repos. 💻

## How to run
1️⃣ First, in the project directory, you must create a json file called: `config.json`, and create json like so:

```
{
  "github_access_token": "my_github_token_that_has_repo_rights",
  "github_account_name": "tylerwilbanks"
}
```
🔐 The reason for this is so you don't check your github access token into source control *(muy malo)*. 🔐

### Next
Run ▶️ the project and behold the results! ✨

### Extra
If you want to configure the file types that will be counted, you can open `Settings.py` and
change the accepted file extensions in the `SUPPORTED_FILE_EXTENSIONS` list.

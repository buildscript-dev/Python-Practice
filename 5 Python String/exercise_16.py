# Exercise 16 -

filename = input("Enter the filename: ")

# Extract extension
file_extension = "." + filename.split(".")[-1]

file_types = [
    ".py", ".pyw", ".pyc", ".pyo",
    ".env", ".ini", ".cfg", ".toml",
    ".yaml", ".yml", ".json", ".xml",
    ".html", ".css", ".js", ".jsx",
    ".ts", ".tsx",
    ".csv", ".xlsx", ".txt",
    ".db", ".sqlite3", ".parquet",
    ".ipynb", ".pkl", ".joblib", ".h5",
    ".png", ".jpg", ".jpeg", ".gif",
    ".svg", ".mp4", ".avi", ".mp3", ".wav",
    ".md", ".rst",
    ".sh", ".bat", ".log", ".tmp", ".bak"
]

# Check if extension is supported
if file_extension in file_types:
    print("You can access the file now....")
else:
    print("File Type Not Supported...")
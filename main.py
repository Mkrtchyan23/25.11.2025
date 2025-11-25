from openpyxl import Workbook
import subprocess
import json

print("Создание git репозитория арам харош")
subprocess.run(["git", "init"])

for i in range(1, 11):
    with open("file.txt", "a", encoding="utf8") as f:
        f.write(f"commit {i}\n")
    subprocess.run(["git", "add", "file.txt"])
    subprocess.run(["git", "commit", "-m", f"aram number {i}"])

print("Коммиты созданы арам харош")


result = subprocess.run(
    ["git", "log", '--pretty=format:{ "hash": "%H", "author": "%an", "email": "%ae", "date": "%ad", "message": "%s" }'],
    stdout=subprocess.PIPE,
    text=True,
    encoding="utf-8"
)


log_lines = result.stdout.splitlines()
log_output = "[" + ",".join(log_lines) + "]"
commits = json.loads(log_output)


wb = Workbook()
ws = wb.active
ws.title = "Git log"
ws.append(["Hash", "Author", "Email", "Date", "Message"])

for c in commits:
    ws.append([c["hash"], c["author"], c["email"], c["date"], c["message"]])

wb.save("git_log.xlsx")
print("Файл создан арам вообще легенда")
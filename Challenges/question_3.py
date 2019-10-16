import re
import os

file1_path = os.path.abspath("input00.txt")
file2_path = os.path.abspath("input01.txt")
file3_path = os.path.abspath("input02.txt")

with open(file1_path, 'r') as f:
    file_content = f.read()
    emails_lists = []
    result = re.findall(r'[\w\.-]+@[\w\.-]+', file_content)
    for email in result:
        emails_lists.append(email)
    lexographical_list = sorted(emails_lists, key=str.lower)

    for email in lexographical_list:
        print(email, end=", ")

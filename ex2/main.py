import csv
import re
from collections import defaultdict
from pprint import pprint
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for contact in contacts_list[1:]:
    full_name = " ".join(contact[:3]).split()
    contact[:3] = (full_name + [""] * 3)[:3]

phone_pattern = re.compile(
    r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s*(доб\.)\s*(\d+))?"
)
phone_format = r"+7(\2)\3-\4-\5\6\7\8"

for contact in contacts_list[1:]:
    contact[5] = phone_pattern.sub(phone_format, contact[5])

contacts_dict = defaultdict(lambda: ["", "", "", "", "", "", ""])  # Создаём шаблон контакта с пустыми полями

for contact in contacts_list[1:]:
    lastname, firstname = contact[0], contact[1]
    key = (lastname, firstname)
    for i in range(len(contact)):
        if contact[i]:
            contacts_dict[key][i] = contact[i]

result_list = [contacts_list[0]] + list(contacts_dict.values())

pprint(result_list)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result_list)

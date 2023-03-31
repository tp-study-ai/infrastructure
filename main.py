import sys
import csv

import psycopg2

conn = psycopg2.connect(database="yutfut",
                        host="127.0.0.1",
                        user="yutfut",
                        password="yutfut",
                        port="5432")

cursor = conn.cursor()


def print_hi(a):
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # print(a)
    # print(len(a))
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if len(a) == 2:
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return ["null"]
    che = []
    key_string = ""

    i = 0
    while True:
        if a[i] == "]":
            break
        if a[i] == '"':
            i += 1
            while True:
                if a[i] == "\\":
                    i += 2
                    continue
                if a[i] == '"':
                    che.append(key_string)
                    key_string = ""
                    i += 1
                    break
                key_string += a[i]
                i += 1
        if a[i] == "[":
            i += 1
            continue
        if a[i] == ":":
            i += 1
            continue
        if a[i] == ",":
            i += 1
            continue
        if a[i] == "\n":
            i += 1
            continue

        if a[i] == " ":
            if key_string != "":
                che.append(key_string)
                key_string = ""
            i += 1
            continue

        key_string += a[i]
        i += 1
        if i >= len(a):
            break
    return che


data = []

csv.field_size_limit(sys.maxsize)
with open('../new_file3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(
            [
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
                row[11],
                row[12],
                row[13],
                row[14],
                row[15],
                row[16],
                row[17],
                row[18]
            ]
        )

print("prec")

for item in data:
    if item == data[0]:
        continue
    cursor.execute(
    '''INSERT INTO task (name, description, public_tests, private_tests, generated_tests, difficulty, cf_contest_id, cf_index, cf_points, cf_rating, cf_tags, time_limit, memory_limit_bytes, link, task_ru, input, output, note) VALUES (E'{0}', E'{1}', ARRAY{2}, ARRAY{3}, ARRAY{4}, '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', E'{14}', E'{15}', E'{16}', E'{17}');'''.format(
        item[0].replace("'", r"\'"), item[1].replace('\\', r"\\").replace("'", r"\'"), print_hi(item[2]), print_hi(item[3]), print_hi(item[4]), item[5], item[6], item[7],
        item[8], item[9], str(item[10].replace("'", "")), item[11], item[12], item[13], item[14].replace('\\', r"\\").replace("'", r"\'"), item[15].replace('\\', r"\\").replace("'", r"\'"), item[16].replace('\\', r"\\").replace("'", r"\'"), item[17].replace('\\', r"\\").replace("'", r"\'")))
    conn.commit()

# [intput: "example" output: "example", intput: "example" output: "example"]
# ['intput', 'example', 'output']

# i = 0
#
# f = open('../init_db/init.sql', 'w')
# for item in data:
#     if item == data[0]:
#         continue
#     i += 1
#     f.write(
#         '''(E'{0}', E'{1}', 'ARRAY{2}', 'ARRAY'{3}', ARRAY'{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', E'{14}', E'{15}', E'{16}', E'{17}'),\n'''.format(
#         item[0].replace("'", r"\'"), item[1].replace('\\', r"\\").replace("'", r"\'"), print_hi(item[2]), print_hi(item[3]), print_hi(item[4]), item[5], item[6], item[7],
#         item[8], item[9], str(item[10].replace("'", "")), item[11], item[12], item[13], item[14].replace('\\', r"\\").replace("'", r"\'"), item[15].replace('\\', r"\\").replace("'", r"\'"), item[16].replace('\\', r"\\").replace("'", r"\'"), item[17].replace('\\', r"\\").replace("'", r"\'")
#         )
#     )
#     if i == 10:
#         break


import sys
import csv

import psycopg2

conn = psycopg2.connect(database="yutfut",
                        host="127.0.0.1",
                        user="yutfut",
                        password="yutfut",
                        port="5432")

cursor = conn.cursor()

class MyString(str):
    def __init__(self, my_object: str):
        self.value = my_object

    def __repr__(self):
        return '$study_ai_tag$' + self.value + '$study_ai_tag$'


def parse_tests(text):
    text = text[1:len(text) - 1]
    che = []
    while (True):
        input = text[0:5]

        text = text[8:]
        pos = text.find('output: "')
        input_case = text[:pos-2].replace('\\n', "\n")

        text = text[pos:]
        output = text[:6]

        text = text[9:]
        pos = text.find('input: "')
        if pos == -1:
            pos = text.find('"')
            output_case = text[:pos].replace('\\n', "\n")

            che.append(MyString(input))
            che.append(MyString(input_case))
            che.append(MyString(output))
            che.append(MyString(output_case))
            if len(che) == 0:
                return ["NULL"]
            return che

        output_case = text[:pos-4].replace('\\n', "\n")
        text = text[pos:]

        che.append(MyString(input))
        che.append(MyString(input_case))
        che.append(MyString(output))
        che.append(MyString(output_case))

data = []


csv.field_size_limit(sys.maxsize)

with open('new_file3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(
            [
                row[1],  # name
                row[2],  # description
                row[3],  # public_tests
                row[4],  # private_tests
                row[5],  # generated_tests
                row[6],  # difficulty
                row[7],  # cf_contest_id
                row[8],  # cf_index
                row[9],  # cf_points
                row[10],  # cf_rating
                row[11],  # cf_tags
                row[12],  # time_limit
                row[13],  # memory_limit_bytes
                row[14],  # link
                row[15],  # task_ru
                row[16],  # input
                row[17],  # output
                row[18]  # note
            ]
        )

for item in data:
    if item == data[0]:
        continue
    if len(item[10]):
        item[10] = ["NULL"]

    cursor.execute(
        '''INSERT INTO tasks (
        name,
        description,
        public_tests,
        private_tests,
        generated_tests,
        difficulty,
        cf_contest_id,
        cf_index,
        cf_points,
        cf_rating,
        cf_tags,
        time_limit,
        memory_limit_bytes,
        link,
        task_ru,
        input,
        output,
        note
        ) VALUES (
        E'{0}',
        E'{1}',
        ARRAY{2},
        ARRAY{3},
        ARRAY{4},
        '{5}',
        {6},
        '{7}',
        '{8}',
        '{9}',
        ARRAY{10},
        '{11}',
        '{12}',
        '{13}',
        E'{14}',
        E'{15}',
        E'{16}',
        E'{17}'
        );'''.format(
            item[0].replace("'", r"\'"),
            item[1].replace('\\', r"\\").replace("'", r"\'"),
            parse_tests(item[2]),
            parse_tests(item[3]),
            parse_tests(item[4]),
            item[5],
            item[6],
            item[7],
            item[8],
            item[9],
            item[10],
            # str(item[10].replace("'", "")),
            item[11],
            item[12],
            item[13],
            item[14].replace('\\', r"\\").replace("'", r"\'"),
            item[15].replace('\\', r"\\").replace("'", r"\'"),
            item[16].replace('\\', r"\\").replace("'", r"\'"),
            item[17].replace('\\', r"\\").replace("'", r"\'")))
    conn.commit()

import sys
import csv

import psycopg2

conn = psycopg2.connect(database="yutfut",
                        host="127.0.0.1",
                        user="yutfut",
                        password="yutfut",
                        port="5432")
cursor = conn.cursor()

# tags_dict = {
#     "*special": "*особая задача",
#     "2-sat": "2-sat",
#     "binary search": "бинарный поиск",
#     "bitmasks": "битмаски",
#     "brute force": "перебор",
#     "chinese remainder theorem": "китайская теорема об остатках",
#     "combinatorics": "комбинаторика",
#     "constructive algorithms": "конструктив",
#     "data structures": "структуры данных",
#     "dfs and similar": "поиск в глубину и подобное",
#     "divide and conquer": "разделяй и властвуй",
#     "dp": "дп",
#     "dsu": "системы непересекающихся множеств",
#     "expression parsing": "разбор выражений",
#     "fft": "быстрое преобразование Фурье",
#     "flows": "потоки",
#     "games": "игры",
#     "geometry": "геометрия",
#     "graph matchings": "паросочетания",
#     "graphs": "графы",
#     "greedy": "жадные алгоритмы",
#     "hashing": "хэши",
#     "implementation": "реализация",
#     "interactive": "интерактив",
#     "math": "математика",
#     "matrices": "матрицы",
#     "meet-in-the-middle": "meet-in-the-middle",
#     "number theory": "теория чисел",
#     "probabilities": "теория вероятностей",
#     "schedules": "расписания",
#     "shortest paths": "кратчайшие пути",
#     "sortings": "сортировки",
#     "string suffix structures": "строковые суфф. структуры",
#     "strings": "строки",
#     "ternary search": "тернарный поиск",
#     "trees": "деревья",
#     "two pointers": "два указателя"
# }

# seconds: 2\n
# seconds: 1\nnanos: 500000000\n
# seconds: 1\n
# seconds: 5\n
# seconds: 3\n
# seconds: 3\nnanos: 500000000\n
# seconds: 4\n
# nanos: 500000000\n
# seconds: 12\n
# seconds: 7\n
# seconds: 2\nnanos: 500000000\n
# seconds: 6\n
# seconds: 8\n
# nanos: 750000000\n
# seconds: 10\n
# seconds: 4\nnanos: 500000000\n
# seconds: 5\nnanos: 500000000\n
# seconds: 2\nnanos: 200000000\n
# seconds: 15\n
# seconds: 6\nnanos: 500000000\n
# seconds: 9\n
# NaN
# seconds: 1\nnanos: 250000000\n
# seconds: 7\nnanos: 500000000\n
# nanos: 400000000\n
# seconds: 1\nnanos: 700000000\n

tags_dict = {
    "*special": 1,
    "2-sat": 2,
    "binary search": 3,
    "bitmasks": 4,
    "brute force": 5,
    "chinese remainder theorem": 6,
    "combinatorics": 7,
    "constructive algorithms": 8,
    "data structures": 9,
    "dfs and similar": 10,
    "divide and conquer": 11,
    "dp": 12,
    "dsu": 13,
    "expression parsing": 14,
    "fft": 15,
    "flows": 16,
    "games": 17,
    "geometry": 18,
    "graph matchings": 19,
    "graphs": 20,
    "greedy": 21,
    "hashing": 22,
    "implementation": 23,
    "interactive": 24,
    "math": 25,
    "matrices": 26,
    "meet-in-the-middle": 27,
    "number theory": 28,
    "probabilities": 29,
    "schedules": 30,
    "shortest paths": 31,
    "sortings": 32,
    "string suffix structures": 33,
    "strings": 34,
    "ternary search": 35,
    "trees": 36,
    "two pointers": 37,
}


def parse_tags(request):
    request = request[2:len(request) - 2]
    if len(request) == 0:
        return [0]
    request = request.split("', '")
    response = []
    for i in request:
        response.append(tags_dict[i])
    return response


class MyString(str):
    def __init__(self, my_object: str):
        self.value = my_object

    def __repr__(self):
        return '$study_ai_tag$' + self.value + '$study_ai_tag$'


def parse_tests(text):
    text = text[1:len(text) - 1]
    che = []
    while True:
        input = text[0:5]
        text = text[8:]
        pos = text.find('output: "')
        input_case = text[:pos - 2].replace('\\n', "\n")

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
        output_case = text[:pos - 4].replace('\\n', "\n")

        text = text[pos:]
        che.append(MyString(input))
        che.append(MyString(input_case))
        che.append(MyString(output))
        che.append(MyString(output_case))


data = []

csv.field_size_limit(sys.maxsize)


def parse_timeout(text):
    che = text.split('\n')
    if len(che[0]) == 0:
        return 1
    if che[0][:7] == "seconds":
        che[0] = int(che[0][9:])
        if len(che[1]) != 0:
            che[1] = int(che[1][7:]) / 1000000000
            che[0] += che[1]
        return che[0]
    if che[0][:5] == "nanos":
        che[0] = int(che[0][7:]) / 1000000000
        return che[0]
    return 1


def parse_url(a, b):
    return "/contest/" + str(a) + "/problem/" + str(b)


with open('../new_file31.csv') as f:
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
                row[15],  # name_ru
                row[16],  # task_ru
                row[17],  # input
                row[18],  # output
                row[19],  # note
            ]
        )

for item in data:
    if item == data[0]:
        continue
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
        short_link,
        name_ru,
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
        {5},
        {6},
        '{7}',
        '{8}',
        '{9}',
        ARRAY{10},
        '{11}',
        '{12}',
        '{13}',
        '{14}',
        E'{15}',
        E'{16}',
        E'{17}',
        E'{18}',
        E'{19}'
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
            parse_tags(item[10]),
            parse_timeout(item[11]),
            item[12],
            item[13],
            parse_url(item[6], item[7]),
            item[14].replace('\\', r"\\").replace("'", r"\'"),
            item[15].replace('\\', r"\\").replace("'", r"\'"),
            item[16].replace('\\', r"\\").replace("'", r"\'"),
            item[17].replace('\\', r"\\").replace("'", r"\'"),
            item[18].replace('\\', r"\\").replace("'", r"\'")))
    conn.commit()

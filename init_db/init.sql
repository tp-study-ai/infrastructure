DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP TABLE IF EXISTS send_task CASCADE;
DROP TABLE IF EXISTS likes CASCADE;

create table tasks
(
    id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(256) NOT NULL,
    description text,
    public_tests text[],
    private_tests text[],
    generated_tests text[],
    difficulty integer,
    cf_contest_id integer,
    cf_index VARCHAR(3),
    cf_points float,
    cf_rating integer,
    cf_tags integer[],
    time_limit float,
    memory_limit_bytes integer,
    link VARCHAR(256),
    short_link VARCHAR(256),
    name_ru text,
    task_ru text,
    input text,
    output text,
    note text
);

CREATE TABLE users (
    id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL,
    cold_start BOOL NOT NULL
);

CREATE TABLE send_task (
    id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id integer NOT NULL,
    task_id integer NOT NULL,
    check_time float,
    build_time float,
    check_result int,
    check_message text,
    tests_passed integer,
    tests_total integer,
    lint_success bool,
    code_text text,
    date TIMESTAMP DEFAULT now() + interval '3 hours' NOT NULL
);

CREATE TABLE likes (
    id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id integer NOT NULL,
    task_id integer NOT NULL
);

CREATE TABLE difficulty_task (
    id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id integer NOT NULL,
    task_id integer NOT NULL,
    difficulty integer NOT NULL
);
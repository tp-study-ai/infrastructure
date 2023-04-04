DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;

SET timezone TO '+03';

create table tasks
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    description text,
    public_tests text[],
    private_tests text[],
    generated_tests text[],
    difficulty text,
    cf_contest_id int,
    cf_index VARCHAR(3),
    cf_points float,
    cf_rating int,
    cf_tags text[],
    time_limit text,
    memory_limit_bytes int,
    link VARCHAR(256),
    task_ru text,
    input text,
    output text,
    note text
);

CREATE TABLE users (
    id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL
);
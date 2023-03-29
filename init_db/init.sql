SET timezone TO '+03';

create table task
(
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    public_tests text[],
    private_tests text[],
    generated_tests text[],
    difficulty text,
    cf_contest_id text,
    cf_index text,
    cf_points text,
    cf_rating text,
    cf_tags text,
    time_limit text,
    memory_limit_bytes text,
    link text,
    task_ru text,
    input text,
    output text,
    note text
);
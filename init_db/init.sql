DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP TABLE IF EXISTS send_task CASCADE;

SET timezone TO '+03';

CREATE OR REPLACE FUNCTION get_ru_date(date TIMESTAMP) RETURNS VARCHAR(30) AS $$
DECLARE
    month_str VARCHAR(30);
    BEGIN
        month_str = CASE to_char(date, 'MM') WHEN '01' THEN ' января '
                        WHEN '02' THEN ' февраля '
                        WHEN '03' THEN ' марта '
                        WHEN '04' THEN ' апреля '
                        WHEN '05' THEN ' мая '
                        WHEN '06' THEN ' июня '
                        WHEN '07' THEN ' июля '
                        WHEN '08' THEN ' августа '
                        WHEN '09' THEN ' сентября '
                        WHEN '10' THEN ' октября '
                        WHEN '11' THEN ' ноября '
                        WHEN '12' THEN ' декабря '
                    END;
        RETURN to_char(date, 'DD')|| month_str || to_char(date, 'YYYY, HH24:MI');
    END;
$$ LANGUAGE plpgsql;

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
    task_ru text,
    input text,
    output text,
    note text
);

CREATE TABLE users (
    id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL
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
    date TIMESTAMP DEFAULT now() NOT NULL
);
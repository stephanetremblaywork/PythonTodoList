CREATE TABLE todo_list (
    name                varchar(255)        NOT NULL
    PRIMARY KEY (name)
);

CREATE TABLE todo_item (
    description         varchar(255)        NOT NULL,
    todo_list_name      varchar(255)        NOT NULL,
    position            int                 NOT NULL,
    is_done             boolean             NOT NULL,
    PRIMARY KEY (description, todo_list_name),
    FOREIGN KEY (todo_list_name)
        REFERENCES todo_list(name)
        ON DELETE CASCADE
)
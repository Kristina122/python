ALTER TABLE users ADD created_new DATETIME, ADD updated_new DATETIME;
UPDATE users SET
    created_new = STR_TO_DATE(created_at, '%d.%m.%Y %h:%i'),
    updated_new = STR_TO_DATE(updated_at, '%d.%m.%Y %h:%i');

ALTER TABLE users DROP created_at, DROP updated_at,
    CHANGE created_new created_at DATETIME,
    CHANGE updated_new updated_at DATETIME;

SELECT * FROM users;
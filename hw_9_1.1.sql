START TRANSACTION;

INSERT INTO sample.users (name) VALUES
    ((SELECT `name` FROM shop.users WHERE id = 1));
DELETE FROM shop.users WHERE id = 1;

COMMIT;


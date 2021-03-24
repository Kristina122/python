CREATE DEFINER=`root`@`localhost` TRIGGER `products_BEFORE_INSERT` BEFORE INSERT ON `products` FOR EACH ROW BEGIN
    IF ((ISNULL(NEW.`name`) or NEW.`name` = '') + (ISNULL(NEW.`description`) or NEW.`description` = '') = 2) THEN
        SIGNAL SQLSTATE '45000'
        SET message_text = 'name and description don''t have value';
	END IF;
END
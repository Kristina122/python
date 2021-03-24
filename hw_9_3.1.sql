CREATE DEFINER=`root`@`localhost` FUNCTION `hello`(h_s DATETIME) RETURNS varchar(50) CHARSET utf8mb4
    READS SQL DATA
BEGIN
  DECLARE day_time VARCHAR(50);
  
  CASE
	  WHEN CAST(h_s AS TIME) BETWEEN CAST('06:00' AS TIME) AND CAST('12:00' AS TIME) THEN 
      SET day_time = 'Доброе утро!';
	  WHEN CAST(h_s AS TIME) BETWEEN CAST('12:00' AS TIME) AND CAST('18:00' AS TIME) THEN 
      SET day_time = 'Добрый день!';
	  WHEN CAST(h_s AS TIME) BETWEEN CAST('18:00' AS TIME) AND CAST('00:00' AS TIME) THEN 
      SET day_time = 'Добрый вечер!';
	  WHEN CAST(h_s AS TIME) BETWEEN CAST('00:00' AS TIME) AND CAST('06:00' AS TIME) THEN 
      SET day_time = 'Доброй ночи!';
      ELSE
      SET day_time = 'Ошибка!';
  END CASE;
  
  RETURN day_time;
END
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `name_catalog` (`id_product` , `product_name` , `catalogs_name`) AS
    SELECT 
        `products`.`id` AS `id`,
        `products`.`name` AS `name`,
        `c`.`name` AS `name`
    FROM
        (`products`
        JOIN `catalogs` `c` ON ((`c`.`id` = `products`.`catalog_id`)))
SELECT 
    products.id,
    products.name,
    catalogs.name
 FROM products
 JOIN catalogs ON catalogs.id = products.catalog_id;
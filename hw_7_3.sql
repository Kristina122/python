SELECT 
    flights.id,
    c.name AS from_name_city,
    c_2.name AS to_name_city
 FROM flights
 JOIN cities c ON c.label = flights.from_city
 JOIN cities c_2 ON c_2.label = flights.to_city;
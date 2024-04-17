

-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;



CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name TEXT,
    average_cooking_time INT,
    rating INT
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (recipe_name, average_cooking_time, rating) VALUES ('Fish and Chips', '20', '3');
INSERT INTO recipes (recipe_name, average_cooking_time, rating) VALUES ('Steak and Eggs', '12', '4');
INSERT INTO recipes (recipe_name, average_cooking_time, rating) VALUES ('Roast Dinner', '60', '5');
INSERT INTO recipes (recipe_name, average_cooking_time, rating) VALUES ('Vegan Nut Roast', '30', '1');
INSERT INTO recipes (recipe_name, average_cooking_time, rating) VALUES ('Korean Fried Chicken and Rice', '25', '5');

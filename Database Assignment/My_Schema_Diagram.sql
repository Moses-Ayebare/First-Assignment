CREATE TABLE `Names` (
  `id` int PRIMARY KEY,
  `person_name` text,
  `username` text,
  `phone_number` int,
  `depature_airport` text
);

CREATE TABLE `Names_Airline` (
  `names_id` int,
  `airline_id` int
);

CREATE TABLE `Airline` (
  `id` int PRIMARY KEY,
  `airline_name` text,
  `travel_class` text,
  `number_of_passengers` int
);

CREATE TABLE `Arrival_Airport` (
  `id` int PRIMARY KEY,
  `airport_name` text
);

CREATE TABLE `Names_Airport` (
  `names_id` int,
  `airport_id` int
);

CREATE TABLE `airline_airport` (
  `airline_id` int,
  `airport_id` int
);

ALTER TABLE `Names_Airline` ADD FOREIGN KEY (`names_id`) REFERENCES `Names` (`id`);

ALTER TABLE `Names_Airline` ADD FOREIGN KEY (`airline_id`) REFERENCES `Airline` (`id`);

ALTER TABLE `Names_Airport` ADD FOREIGN KEY (`names_id`) REFERENCES `Names` (`id`);

ALTER TABLE `Names_Airport` ADD FOREIGN KEY (`airport_id`) REFERENCES `Arrival_Airport` (`id`);

ALTER TABLE `airline_airport` ADD FOREIGN KEY (`airline_id`) REFERENCES `Airline` (`id`);

ALTER TABLE `airline_airport` ADD FOREIGN KEY (`airport_id`) REFERENCES `Arrival_Airport` (`id`);


CREATE TABLE `position`
(
 `position_id`          integer NOT NULL AUTO_INCREMENT ,
 `position_description` varchar(45) NOT NULL ,

PRIMARY KEY (`position_id`)
);

insert into position (position_description)
values
("Centre-right"),
("Right-wing"),
("Centre"),
("Centre-left"),
("Far-right"),
("Left-wing");

CREATE TABLE `politician`
(
 `politician_id` integer NOT NULL AUTO_INCREMENT ,
 `name`          varchar(30) NOT NULL ,
 `party_id`      integer NOT NULL ,

PRIMARY KEY (`politician_id`)
);

CREATE TABLE `party`
(
 `party_id`     integer NOT NULL AUTO_INCREMENT ,
 `name`         varchar(30) NOT NULL ,
 `seats`        integer NOT NULL ,
 `party_leader` integer NOT NULL ,
 `position_id`  integer NOT NULL ,

PRIMARY KEY (`party_id`),
KEY `fkIdx_14` (`party_leader`),
CONSTRAINT `FK_13` FOREIGN KEY `fkIdx_14` (`party_leader`) REFERENCES `politician` (`politician_id`),
KEY `fkIdx_26` (`position_id`),
CONSTRAINT `FK_25` FOREIGN KEY `fkIdx_26` (`position_id`) REFERENCES `position` (`position_id`)
);

ALTER TABLE politician
ADD FOREIGN KEY `fkIdx_11` (`party_id`) REFERENCES `party` (`party_id`);

CREATE TABLE `recommendation`
(
 `recommendation_id`   integer NOT NULL AUTO_INCREMENT ,
 `recommendation_date` date NOT NULL ,
 `recommendation_desc` varchar(255) NOT NULL ,
 `recommended_by`      integer NOT NULL ,

PRIMARY KEY (`recommendation_id`)
);

CREATE TABLE `government`
(
 `gov_number`        integer NOT NULL ,
 `prime_min`         integer NOT NULL ,
 `start_date`        date NOT NULL ,
 `recommendation_id` integer NOT NULL ,

PRIMARY KEY (`gov_number`),
KEY `fkIdx_33` (`prime_min`),
CONSTRAINT `FK_32` FOREIGN KEY `fkIdx_33` (`prime_min`) REFERENCES `politician` (`politician_id`),
KEY `fkIdx_86` (`recommendation_id`),
CONSTRAINT `FK_85` FOREIGN KEY `fkIdx_86` (`recommendation_id`) REFERENCES `recommendation` (`recommendation_id`)
);

CREATE TABLE `ideology`
(
 `ideology_name` varchar(45) NOT NULL ,
 `ideology_id`   integer NOT NULL AUTO_INCREMENT ,

PRIMARY KEY (`ideology_id`)
);

insert into ideology (ideology_name)
values 
("National Liberalism"),
("Liberalism"),
("Religious Conservatism"),
("Social Liberalism"),
("Social Democracy"),
("National Secularism"),
("Religious Zionism"),
("Big tent"),
("Majority interests"),
("Islamism");

CREATE TABLE `party_ideology`
(
 `party_id`    integer NOT NULL ,
 `ideology_id` integer NOT NULL ,

PRIMARY KEY (`party_id`, `ideology_id`),
KEY `fkIdx_74` (`party_id`),
CONSTRAINT `FK_73` FOREIGN KEY `fkIdx_74` (`party_id`) REFERENCES `party` (`party_id`),
KEY `fkIdx_80` (`ideology_id`),
CONSTRAINT `FK_79` FOREIGN KEY `fkIdx_80` (`ideology_id`) REFERENCES `ideology` (`ideology_id`)
);

CREATE TABLE `recommendation_party`
(
 `party_id`          integer NOT NULL ,
 `recommendation_id` integer NOT NULL ,
 `seats`             integer NOT NULL ,
 `party_leader`      integer NOT NULL ,

PRIMARY KEY (`party_id`, `recommendation_id`),
KEY `fkIdx_64` (`party_leader`),
CONSTRAINT `FK_63` FOREIGN KEY `fkIdx_64` (`party_leader`) REFERENCES `politician` (`politician_id`),
KEY `fkIdx_67` (`party_id`),
CONSTRAINT `FK_66` FOREIGN KEY `fkIdx_67` (`party_id`) REFERENCES `party` (`party_id`),
KEY `fkIdx_70` (`recommendation_id`),
CONSTRAINT `FK_69` FOREIGN KEY `fkIdx_70` (`recommendation_id`) REFERENCES `recommendation` (`recommendation_id`)
);
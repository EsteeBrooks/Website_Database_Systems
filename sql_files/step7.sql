ALTER TABLE politician DROP FOREIGN KEY politician_ibfk_1;

ALTER TABLE politician DROP COLUMN party_id;

INSERT INTO politician(name) VALUES  
("Benjamin Netanyahu"),     
("Yair Lapid"),     
("Aryeh Deri"),     
("Benny Gantz"),     
("Naftali Bennett"),     
("Merav Michaeli"),     
("Moshe Gafni"),     
("Avigdor Lieberman"),     
("Bezalel Smotrich"),     
("Ayman Odeh"),     
("Gideon Sa'ar"),    
("Nitzan Horowitz"),     
("Mansour Abbas");

INSERT INTO party (name, seats, party_leader, position_id) VALUES  
	("Likud", 30, 1, 1),     
    ("Yesh Atid", 17, 2, 3),     
    ("Shas", 9, 3, 2),     
    ("Blue and White", 8, 4, 3),     
    ("Yamina", 7, 5, 2),     
    ("Labor", 7, 6, 4),     
    ("United Torah Judaism", 7, 7, 2),     
    ("Yisrael Beiteinu", 7, 8, 1),     
    ("Religious Zionist", 6, 9, 5),     
    ("Joint List", 6, 10, 6),     
    ("New Hope", 6, 11, 2),     
    ("Meretz", 6, 12, 6),     
    ("Ra'am", 4, 13, 6);
    
INSERT INTO party_ideology VALUES
	(1,1), # Likud	    National liberalism
    (2,2), # Yesh Atid	Liberalism
    (3,3), # Shas	    Religious conservatism
    (4,4), # Blue and White.  	Social liberalism
    (5,5), # Yamina	    National conservatism
    (6,6), # Labor	    Social democracy
    (7,3), # United Torah Judaism. 	 Religious conservatism
    (8,6), # Yisrael Beiteinu	Nationalism Secularism
    (8,7),
    (9,8),
    (9,9),
    (10,),
    (11,),
    (12,),
    (13,);
    

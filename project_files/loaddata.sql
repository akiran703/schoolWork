CREATE TABLE IF NOT EXISTS exercise (
	Exercise TEXT NOT NULL,
    Equipment TEXT NOT NULL,
    ExerciseType TEXT NOT NULL,
    MajorMuscle TEXT NOT NULL,
    MinorMuscle TEXT NOT NULL,
    Example TEXT NOT NULL,
    Notes TEXT NOT NULL,
    Modifications TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS userdatabase(
    Username text not null,
    email text not null,
    password text not null
);


CREATE TABLE IF NOT EXISTS dishes(
    name	text not null,
    id	integer not null,
    minutes	integer not null,
    contributor_id	integer not null,
    submitted	text not null,
    tags	text not null,
    nutrition	text not null,
    n_steps	integer not null,
    steps	text not null,
    description	text not null,
    ingredients	text not null,
    n_ingredients integer not null
);

CREATE TABLE IF NOT EXISTS user_entered_exercise (
	Exercise TEXT NOT NULL,
    Equipment TEXT NOT NULL,
    ExerciseType TEXT NOT NULL,
    MajorMuscle TEXT NOT NULL,
    MinorMuscle TEXT NOT NULL,
    Example TEXT NOT NULL,
    Notes TEXT NOT NULL,
    Modifications TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS user_entered_dishes(
    name	text not null,
    id	integer not null,
    minutes	integer not null,
    contributor_id	integer not null,
    submitted	text not null,
    tags	text not null,
    nutrition	text not null,
    n_steps	integer not null,
    steps	text not null,
    description	text not null,
    ingredients	text not null,
    n_ingredients integer not null
);



CREATE TABLE IF NOT EXISTS user_food(
    password text not null,
    dish_name text not null
);

CREATE TABLE IF NOT EXISTS user_exercise(
    password text not null,
    exercise_name text not null
);

CREATE TABLE IF NOT EXISTS user_food_entered(
    password text not null,
    dish_name_entered text not null
);

CREATE TABLE IF NOT EXISTS user_exercise_entered(
    password text not null,
    exercise_name_entered text not null
);

CREATE TABLE IF NOT EXISTS user_entered_exercise (
	Exercise TEXT NOT NULL,
    Equipment TEXT NOT NULL,
    ExerciseType TEXT NOT NULL,
    MajorMuscle TEXT NOT NULL,
    MinorMuscle TEXT NOT NULL,
    Example TEXT NOT NULL,
    Notes TEXT NOT NULL,
    Modifications TEXT NOT NULL,
    usernameid TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS user_entered_dishes(
    name	text not null,
    id	integer not null,
    minutes	integer not null,
    contributor_id	integer not null,
    submitted	text not null,
    tags	text not null,
    nutrition	text not null,
    n_steps	integer not null,
    steps	text not null,
    description	text not null,
    ingredients	text not null,
    n_ingredients integer not null,
    usernameid TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tagFilter(
    name    text not null,
    tags    text not null
);
INSERT INTO tagFilter SELECT name, tags FROM dishes;

CREATE TABLE IF NOT EXISTS MajorMuscleFilter(
    Exercise    text not null,
    MajorMuscle    text not null
);
INSERT INTO MajorMuscleFilter SELECT exercise, MajorMuscle FROM Exercise;

CREATE TABLE IF NOT EXISTS weekPlan(
    dish_name text not NULL,
    exercise_name text not null,
    week_name text not NULL
);

ALTER TABLE dishes DROP COLUMN tags;
ALTER TABLE exercise DROP COLUMN MajorMuscle;
ALTER TABLE exercise DROP COLUMN MinorMuscle;

--1
--created users
insert into userdatabase(Username,email,password)
values('KA','kashokkumar@ucmerced.edu','kiran'),
('HV','Hvillasin@ucmerced.edu','hannah'),
('BS','bsingh@ucmerced.edu','baljot'),
('PM','pmendoza@ucmerced.edu','peter'),
('SL','sli@ucmerced.edu','sean');

--2
--input into the user entered dish table
insert into user_entered_dishes(name,id,minutes,contributor_id,submitted,tags,nutrition,n_steps,steps,description,ingredients,n_ingredients,usernameid)
VALUES( 'fried rice',1,60,1,'2021-11-11','chicken,healthy,high-fat,high-sodium','330,5,8,10,6,11,0',3,'cook rice,grill chicken,cook vegtables, mix everthing',
        'a dish if you are trying to eat something with weight to it','rice,chicken,vegetables',3,'KA');

--3
--user inputs a exercise that doesnt exist in the data
insert into user_entered_exercise(Exercise,Equipment,ExerciseType,MajorMuscle,MinorMuscle,Example,Notes,Modifications,usernameid)
values('Bench Press','bench,bar','Weight','Chest','', 'some gif goes here','arch your back,control the motion','none','HV');

--4
--insert values into the joining table of the user entered dishes and exercises
INSERT INTO user_exercise_entered (password, exercise_name_entered)
VALUES ('hannah', 'Bench Press');

--5
INSERT INTO user_food_entered (password, dish_name_entered)
VALUES ('kiran', 'fried rice');

--6
-- importing exercise (from exercise table) that the user wants to saved into user_exercise table
INSERT INTO user_exercise (password, exercise_name)
VALUES ('hannah', 'Frogger'),
 ('hannah', 'High Knees'),
 ('hannah', 'Pushup'),
 ('hannah', 'Russian Twist'),
 ('hannah', 'Halo'),
 ('hannah', 'Glute Bridge'),
 ('hannah', 'Kettlebell Swing'),
 ('hannah', 'Broad Jump'),
 ('hannah','Calf Raise'),
 ('hannah','Compass Jump'),
 ('hannah','Butt Kickers'),
 ('hannah','Donkey Kick'),
 ('hannah','Frogger'),
 ('hannah','Deficit Squat');


insert into user_food(password,dish_name)
values('hannah', 'hawaiian  chicken salad appetizer'),
('hannah', 'jamaican me hungry  chicken bake'),
('hannah','leftovers  dessert'),
('hannah','meal in a bowl   guacamole salad'),
('hannah','pparty  taco dip'),
('hannah','cream  of cauliflower soup  vegan'),
('hannah','grilled  ranch bread'),
('hannah','i can t believe it s spinach'),
('hannah','jiffy  extra moist carrot cake'),
('hannah','killer  lasagna'),
('hannah','beat this  banana bread'),
('hannah','rich  hot fudge cake'),
('hannah','some like it hot'),
('hannah','sour cream  avocado dip  vegan');


--7
-- 6&7 are together. inserting values into the weekplan by using SELECT query. leaving dish_name and week_name as no values while for the exercise_name we are importing it using SELECT statement from user_exercise table (can be done using exercise_name_entered table)
INSERT INTO weekPlan(dish_name, exercise_name, week_name)
values 
       ('leftovers  dessert','High Knees','Monday'),
       ('jamaican me hungry  chicken bake','Pushup','Tuesday'),
       ( 'meal in a bowl   guacamole salad','Russian Twist','Tuesday'),
       ( 'cream  of cauliflower soup  vegan','Glute Bridge','Wednesday'),
       ( 'grilled  ranch bread', 'Kettlebell Swing','Wednesday'),
       ( 'i can t believe it s spinach','Broad Jump','Thursday'),
       ('jiffy  extra moist carrot cake','Calf Raise','Thursday'),
       ('killer  lasagna','Compass Jump','Friday');


--8
-- Updating weekPlan table by setting the two other columns based on the user preseference
UPDATE weekPlan
SET week_name = 'Monday', dish_name = 'alouette  potatoes'
WHERE exercise_name = 'Arnold Press';

--9
--delete a dish or exercise a user doesnt want to do( will have to make sure the passwords line up with the user)
DELETE from user_exercise where exercise_name = 'Butt Kickers' and password = 'kiran'

--10
-- DELETES DUPLICATE exercise FROM user_exercise_entered. For example, if user have saved two same excercise name, it will delete one
DELETE FROM user_exercise_entered 
WHERE rowid NOT IN 
    (SELECT min(rowid) 
    FROM user_exercise_entered 
    GROUP BY password, exercise_name_entered);

--11
-- Outputs the number of exercises that targets a specific muscle. Can be done on exercise and user_entered_exercise table
-- Change '%Arms%' to a different value.
SELECT MF.MajorMuscle, count(E.Exercise) as numOfExercise
FROM Exercise E
INNER JOIN MajorMuscleFilter MF
ON E.Exercise = MF.Exercise
WHERE MF.MajorMuscle LIKE '%Arms%';

--12
-- Outputs the dishes that has that specific tags. Can be done on dishes and user_entered_dishes table
-- Change '%easy%' to a different value
SELECT D.name
FROM Dishes D
INNER JOIN tagFilter TF
ON D.name = TF.name
WHERE TF.tags LIKE '%easy%'

--13
-- Outputs the exercise name & its corresponding muscle group. Can be done on exercise and user_entered_exercise table
SELECT E.Exercise as exercise, MF.MajorMuscle as MajorMuscle
FROM Exercise E
INNER JOIN MajorMuscleFilter MF
ON E.Exercise = MF.Exercise

--14
-- prints the exercise information depending on the user
-- change password value
SELECT *
FROM Exercise E
WHERE E.exercise IN (select exercise_name from user_exercise where password = 'kiran')

--15
-- prints the dish information depending on the user and the week name
SELECT *
FROM Dishes D, user_food UF
WHERE UF.dish_name = D.name
AND UF.password = 'hannah'
AND D.name IN 
    (select dish_name from weekPlan where week_name = 'Monday')

--16
-- prints the exercise information depending on the user and the week name
SELECT *
FROM exercise, user_exercise
WHERE exercise.exercise = user_exercise.exercise_name
AND user_exercise.password = 'hannah'
AND exercise.exercise IN 
    (select exercise_name from weekPlan where week_name = 'Tuesday')


--17
-- searching foods that take less than or equal to a hour and are pies and tarts
select dishes.name
from dishes,tagFilter
where dishes.name = tagFilter.name 
    and dishes.minutes <= 60 
    and tagFilter.tags  LIKE '%pies-and-tarts%'

--18
--outputs the number of dishes that specific user saved for each day
SELECT week_name, count(dish_name) as numOfDishes
FROM weekPlan
WHERE dish_name IN (select dish_name from user_food where password = 'hannah')
GROUP BY week_name

--19
--Outputs the number of saved exercises (created and from search)
SELECT S.numOfInputEx+E.numOfSavedEx
FROM(SELECT IFNULL(N1, 0) as numOfInputEx
    FROM (SELECT username, password FROM userdatabase) R
    LEFT OUTER JOIN
        (SELECT pass,IFNULL(num, 0) as N1
        FROM (SELECT U.password as pass, count(exercise_name_entered) as num
                FROM user_exercise_entered UE, userdatabase U
                WHERE U.password = UE.password
                AND U.password = 'fish') U1) W
    ON R.password = W.pass
    WHERE R.password = 'fish') S,
    (SELECT IFNULL(N2, 0) as numOfSavedEx
    FROM (SELECT username, password FROM userdatabase) R
    LEFT OUTER JOIN
        (SELECT pass,IFNULL(num, 0) as N2
        FROM (SELECT U.password as pass, count(exercise_name) as num
                FROM user_exercise UE, userdatabase U
                WHERE U.password = UE.password
                AND U.password = 'fish') U2) W1
    ON R.password = W1.pass
    WHERE R.password = 'fish') E
-- for dishes
SELECT S.numOfInputD+E.numOfSavedD
FROM(SELECT IFNULL(N1, 0) as numOfInputD
    FROM (SELECT username, password FROM userdatabase) R
    LEFT OUTER JOIN
        (SELECT pass,IFNULL(num, 0) as N1
        FROM (SELECT U.password as pass, count(dish_name_entered) as num
                FROM user_food_entered UD, userdatabase U
                WHERE U.password = UD.password
                AND U.password = 'fish') U1) W
    ON R.password = W.pass
    WHERE R.password = 'fish') S,
    (SELECT IFNULL(N2, 0) as numOfSavedD
    FROM (SELECT username, password FROM userdatabase) R
    LEFT OUTER JOIN
        (SELECT pass,IFNULL(num, 0) as N2
        FROM (SELECT U.password as pass, count(dish_name) as num
                FROM user_food UD, userdatabase U
                WHERE U.password = UD.password
                AND U.password = 'fish') U2) W1
    ON R.password = W1.pass
    WHERE R.password = 'fish') E

--20
-- Outputs the number of dish and exercise in each day of the week for a certain user
SELECT R1.week_name, IFNULL(numD, 0) as numOfDish, IFNULL(numE, 0) as numOfExercise
FROM (SELECT username, password FROM userdatabase) R
LEFT OUTER JOIN
    (SELECT UE.password, week_name, count(W.dish_name) as numD, count(W.exercise_name) as numE
    FROM weekPlan W, user_food UF, user_exercise UE
    WHERE UF.dish_name = W.dish_name
    AND UE.exercise_name = W.exercise_name
    AND UE.password = UF.password
    AND UF.password = 'fish'
    GROUP BY week_name) R1
ON R.password = R1.password
WHERE R.password = 'fish'



SELECT UE.password, week_name, (W.dish_name) as numD, (W.exercise_name) as numE
    FROM weekPlan W, user_food UF, user_exercise UE
    WHERE UF.dish_name = W.dish_name
    AND UE.exercise_name = W.exercise_name
    AND UE.password = UF.password


--healthy soup 2 30 2  2021-11-11  chicken,healthy,low-sodium    150,2,3,11,8,20,1   cut everything,boil all stuff
--2  healthy soup   chicken,water,vegetables   3   kkak

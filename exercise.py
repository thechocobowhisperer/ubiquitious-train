import sqlite3

# from wmt import Exercise

#Change connect(thishing) to exercise.db when testing is complete
conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('exercise.db')
print("Opened database successfully")
c = conn.cursor()

c.execute("""CREATE TABLE EXERCISE (
                NAME TEXT NOT NULL UNIQUE,
                ARMS INT,
                CHEST INT,
                SHOULDERS INT,
                BACK INT,
                CORE INT,
                LEGS INT,
                BASEWEIGHT INT,
                BASESETS INT,
                BASEREPS INT,
                FAVORITE INT
                )""")
print("'EXERCISE' table created successfully")

c.execute("""CREATE TABLE EXERCISETYPE (
                STRENGTH INT,
                STRETCH INT,
                ENDURANCE INT
                )""")
print("'EXERCISETYPE' table created successfully")

c.execute("""CREATE TABLE USER (
                NAME INT NOT NULL,
                HEIGHTIN FLOAT NOT NULL,
                WEIGHT FLOAT NOT NULL,
                AGE INT NOT NULL,
                SEX CHARACTER(1)
                )""")
print("'USER' table created successfully")

c.execute("""CREATE TABLE WORKOUTS (
                OCCURRED TEXT
                 )""")
print("'WORKOUTS' table created successfully")

user_list = []

class User():
    def __init__(self, name, height, weight, age, sex):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        user_list.append(self)
        
    # def doExer(self, exercise):
    #     print(self.name + " did " + exercise.name + " " + str(exercise.sets) + " x " + str(exercise.reps))
user_name = input("What is your name?")
user_height = input("What is your height in inches?")
user_weight = input("What is your weight in pounds(tenths are ok)?")
user_age = input("What is your age?")
user_sex = input("What is your sex?")
my_user = User(user_name, user_height, user_weight, user_age, user_sex)

exer_list = []
class Exercise():
    def __init__(self, name, arms=0, shoulders=0, chest=0, back=0, core=0,
                 legs=0, weight=0, sets=0, reps=0, favorite=0):
        self.name = name
        self.arms = arms
        self.shoulders = shoulders
        self.chest = chest
        self.back = back
        self.core = core
        self.legs = legs
        self.weight = weight
        self.sets = sets
        self.reps = reps       
        self.favorite = favorite
        exer_list.append(self)
        
#Make instance of EACH exercise
single_arm_curl = Exercise('Single Arm Curl',arms=1, weight=15,sets=3,
                           reps=15,favorite=1)
pushups = Exercise('Push-ups', 1, 1, 1, 0, 1, 0, 0, 3, 15, 1)
barbell_curl = Exercise('Barbell Curl', 1, 0, 0, 0, 0, 0, 45, 3, 15, 0)
weighted_row = Exercise(name='Weighted Row', arms=1, shoulders=1,
                        back=1, weight=110, sets=3, reps=15)
chest_press = Exercise(name='Chest Press', arms=1, chest=1, weight=120, sets=3,
                       reps=15, favorite=1)

#  = Exercise(6,'', 1, 0, 0, 0, 0, 0, 15, 3, 15, 1)
# single_arm_curl = Exercise('single arm curl', 1, 0, 0, 0, 0, 0, 15, 3, 15, 1)


def insertExerTable(exer_list):
    with conn:
        for exer in exer_list:
            c.execute("""INSERT INTO exercise VALUES (
                :name,:arms,:chest,:shoulders,:legs,:back,:core,
                :weight,:sets,:reps,:favorite)""", {'name': exer.name,
                'arms': exer.arms,'chest':exer.chest, 'shoulders': exer.shoulders,
                'legs': exer.legs,'back':exer.back, 'core': exer.core, 
                'weight':exer.weight,'sets':exer.sets,'reps':exer.reps,
                'favorite':exer.favorite})
            print(str(exer.name) + " added to 'exercise' table successfully")

#Run insert_exer for EACH exercise to add to exercise.db        
insertExerTable(exer_list)

conn.commit()

#Create functions for each attribute filter
#Make sure to return c.fetchall()/c.fetchmany()/c.fetchone() depending

#Print every entry as its own row
# for row in c.execute("SELECT * FROM exercise"):
#     print (row)

#Returns 1
#print(c.fetchone())
#Returns number specified if possible
#print(c.fetchmany(5))
#Returns all available
# print(c.fetchall())
conn.commit()
print("Executions committed successfully")

conn.close()
print("Database closed successfully")
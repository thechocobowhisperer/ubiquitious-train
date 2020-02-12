import sqlite3

# from wmt import Exercise

#Change connect(thishing) to exercise.db when testing is complete
conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('exercise.db')

c = conn.cursor()

c.execute("""CREATE TABLE exercise (
                name text,
                arms integer,
                chest integer,
                shoulders integer,
                back integer,
                core integer,
                legs integer,
                weight integer,
                sets integer,
                reps integer,
                favorite integer
                )""")

class User():
    def __init__(self, name, height, weight, age, sex):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        
    def doExer(self, exercise):
        print(self.name + " did " + exercise.name + " " + str(exercise.sets) + " x " + str(exercise.reps))

user = User('Joe', 72, 185, 24, 'male')

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
        #TODO
        #Add strength, stretch, and endurance tag attributes for SQL filtering
        
#Make instance of EACH exercise
single_arm_curl = Exercise('single arm curl',arms=1, weight=15,sets=3,
                           reps=15,favorite=1)
pushups = Exercise('pushups', 1, 1, 1, 0, 1, 0, 0, 3, 15, 1)
barbell_curl = Exercise('barbell curl', 1, 0, 0, 0, 0, 0, 45, 3, 15, 0)
weighted_row = Exercise(name='weighted row', arms=1, shoulders=1,
                        back=1, weight=110, sets=3, reps=15)
chest_press = Exercise(name='chest press', arms=1, chest=1, weight=120, sets=3, reps=15, favorite=1)
#  = Exercise(6,'', 1, 0, 0, 0, 0, 0, 15, 3, 15, 1)
# single_arm_curl = Exercise('single arm curl', 1, 0, 0, 0, 0, 0, 15, 3, 15, 1)


def insert_exer(exer_list):
    with conn:
        for exer in exer_list:
            c.execute("""INSERT INTO exercise VALUES (
                :name,:arms,:chest,:shoulders,:legs,:back,:core,
                :weight,:sets,:reps,:favorite)""", {'name': exer.name,
                'arms': exer.arms,'chest':exer.chest, 'shoulders': exer.shoulders,
                'back':exer.back, 'core': exer.core, 'legs': exer.legs,
                'weight':exer.weight,'sets':exer.sets,'reps':exer.reps,
                'favorite':exer.favorite})

#Run insert_exer for EACH exercise to add to exercise.db        
insert_exer(exer_list)

conn.commit()

#Create functions for each attribute filter
#Make sure to return c.fetchall()/c.fetchmany()/c.fetchone() depending
#Print every entry as its own row
for row in c.execute("SELECT * FROM exercise WHERE LEGS IS NOT 1"):
    print (row)

#Returns 1
#print(c.fetchone())
#Returns number specified if possible
#print(c.fetchmany(5))
#Returns all available
# print(c.fetchall())
conn.commit()

conn.close()

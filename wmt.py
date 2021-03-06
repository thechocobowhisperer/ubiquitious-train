
# coding: utf-8
import pandas as pd

# In[ ]:
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


class Exercise():
    def __init__(self, name, push, pull, arms, shoulders, chest, back, core, legs, favorite):
        self.name = name
        self.push = push
        self.pull = pull
        self.arms = arms
        self.shoulders = shoulders
        self.chest = chest
        self.back = back
        self.core = core
        self.legs = legs
        self.favorite = favorite
        self.exer_list.append(self)
        
    
    exer_list = []
    arms_list = []
    chest_list = []
    shoulders_list = []
    back_list = []
    core_list = []
    legs_list = []
    
    
    #Function to show exercises for Arms    
    def forArms():
        Exercise.arms_list = []
        for exercise in Exercise.exer_list:
            if exercise.arms == True:
                Exercise.arms_list.append(exercise)
                Exercise.arms_list = list(set(Exercise.arms_list))
        for item in Exercise.arms_list:
            print(item.name)
    
    #Function to show exercises for Chest    
    def forChest():
        Exercise.chest_list = []
        for exercise in Exercise.exer_list:
            if exercise.chest == True:
                Exercise.chest_list.append(exercise)
                Exercise.chest_list = list(set(Exercise.chest_list))
        for item in Exercise.chest_list:
            print(item.name)
    #Function to show exercises for Shoulders
    def forShoulders():
        Exercise.shoulders_list = []
        for exercise in Exercise.exer_list:
            if exercise.shoulders == True:
                Exercise.shoulders_list.append(exercise)
                Exercise.shoulders_list = list(set(Exercise.shoulders_list))
        for item in Exercise.shoulders_list:
            print(item.name)
    
    #Function to show exercises for Legs    
    def forLegs():
        Exercise.legs_list = []
        for exercise in Exercise.exer_list:
            if exercise.legs == True:
                Exercise.legs_list.append(exercise)
                Exercise.legs_list = list(set(Exercise.legs_list))
        for item in Exercise.legs_list:
            print(item.name)
        
    #Function to show exercises for Back    
    def forBack():
        Exercise.chest_list = []
        for exercise in Exercise.exer_list:
            if exercise.back == True:
                Exercise.back_list.append(exercise)
                Exercise.back_list = list(set(Exercise.back_list))
        for item in Exercise.back_list:
            print(item.name)
            
    #Function to show exercises for Core    
    def forCore():
        Exercise.core_list = []
        for exercise in Exercise.exer_list:
            if exercise.core == True:
                Exercise.core_list.append(exercise)
                Exercise.core_list = list(set(Exercise.core_list))
        for item in Exercise.core_list:
            print(item.name)
    
    # #Function to show exercises for Pulling    
    # def forPull():
    #     for exercise in Exercise.exer_list:
    #         if exercise.pull == True:
    #             return exercise
    
    # #Function to show exercises for Pushing   
    # def forPush():
    #     for exercise in Exercise.exer_list:
    #         if exercise.push == True:
    #             return exercise
    
    
            
            
class RepSet(Exercise):
   def __init__(self, name, push, pull, arms, shoulders, chest, back, core, legs, favorite, weight, reps, sets):
       super().__init__(name, push, pull, arms, shoulders, chest, back, core, legs, favorite)
       self.weight = weight
       self.reps = reps
       self.sets = sets
       progress_counter = 0
       base_reps = reps
       base_weight = weight
       progress_counter = 1
       suggest_rep_incr = base_reps * 1.2 * progress_counter
       suggest_weight_incr = base_weight * 1.2 * progress_counter
       
   
class Stretch(Exercise):
    def __init__(self, name, push, pull, arms, shoulders, chest, back, core, legs, favorite, duration):
       super().__init__(name, push, pull, arms, shoulders, chest, back, core, legs, favorite)
       self.duration = duration
       progress_counter = 0
       progress_counter = 1
       suggest_rep_incr = base_reps * 1.2 * progress_counter
       suggest_weight_incr = base_weight * 1.2 * progress_counter

     
       
class Cardio(Exercise):
    def __init__(self, distance, duration, cardio):
        #Distance in Miles
        self.distance = float(distance)
        #Duration in Minutes
        self.duration = float(duration)
        self.cardio = cardio
        self.speed = self.distance/float(self.duration/60)
        suggest_dist_incr = distance * 1.2 * progress_counter
        suggest_durat_incr = duration * 1.2 * progress_counter
        
        
# pushups = RepSet('pushups', True, False, True, True, True, False, True, False, True, 0, 15, 3)
# chest_press = RepSet('chest_press', True, False, True, True, True, False, False, False, True, 80, 15, 3)
# bicep_stretch = Exercise('bicep_stretch', False, True, False, True, True, False, False, False, False)





# running = Cardio(3, 60, True)


# In[2]:


wmt_dict = {'pushup' : {
    'push':True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': False
    },
    'chest_press': {
    'push':True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'bicep_curl': {
    'push': False, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': False
    },    
    'tricep_extension': {
    'push': True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'weighted_row': {
    'push': True, 
    'pull': False,
    'arms': True,
    'chest': False,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'chest_fly': {
    'push': True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'treadmill': {
    'push': True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'stair_machine': {
    'push': True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'elliptical': {
    'push': True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'bodyweight_squat': {
    'push': True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'leg_curl': {
    'push': True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'leg_extension': {
    'push': True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'dead_lift': {
    'push': True, 
    'pull': True,
    'arms': True,
    'chest': True,
    'back': True,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': False
    },
    'chin_up': {
    'push': False, 
    'pull': True,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'plank': {
    'push': True, 
    'pull': False,
    'arms': True,
    'chest': True,
    'back': False,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    'lat_pulldown': {
    'push': False, 
    'pull': True,
    'arms': True,
    'chest': True,
    'back': True,
    'core': True,
    'legs': False,
    'cardio': False,
    'favorite': True
    },
    }
    
   


# In[3]:


#Print Push Exercises From Dictionary
for e in wmt_dict:
    if (wmt_dict[e]['push'] == True):
        print (e)


# In[4]:


#Print Pull Exercises From Dictionary
for e in wmt_dict:
    if (wmt_dict[e]['pull'] == True):
        print (e)


# In[5]:


#Print Cardio Exercises From Dictionary
for e in wmt_dict:
    if (wmt_dict[e]['cardio'] == True):
        print (e)


# In[6]:


#Print Arm Exercises From Dictionary
for e in wmt_dict:
    if (wmt_dict[e]['arms'] == True):
        print (e)


# In[7]:


#Print Leg Exercises From Dictionary
for e in wmt_dict:
    if (wmt_dict[e]['legs'] == True):
        print (e)


# In[8]:


#Print Chest Exercises From Dictionary
for e in wmt_dict:
    if (wmt_dict[e]['chest'] == True):
        print (e)


# In[9]:


#Print Back Exercises From Dictionary
for e in wmt_dict:
    if (wmt_dict[e]['back'] == True):
        print (e)


# In[10]:


#Print Favorite Exercises From Dictionary
for e in wmt_dict:
    if (wmt_dict[e]['favorite'] == True):
        print (e)


# In[11]:


#Add New Exercise and Set True/False per 
#wmt_dict['Exercise'][15] = 'lat_pulldown'
#wmt_dict['Back'][15] = True
#wmt_dict['Pull'][15] = True
#wmt_dict['Push'][15] = False
#wmt_dict['Arms'][15] = True
#wmt_dict['Legs'][15] = False
#wmt_dict['Cardio'][15] = False
#wmt_dict['Core'][15] = False
#wmt_dict['Chest'][15] = False


# In[12]:


#Add Exercise to wmt_dict
def addExer(name, push, pull, arms, chest, back, legs, core, cardio, favorite):
    if (name not in wmt_dict['Exercise'].values()):
        wmt_dict['Exercise'][len(wmt_dict['Exercise'])] = name
        wmt_dict['Push'][len(wmt_dict['Exercise'])] = push
        wmt_dict['Pull'][len(wmt_dict['Exercise'])] = pull
        wmt_dict['Arms'][len(wmt_dict['Exercise'])] = arms
        wmt_dict['Chest'][len(wmt_dict['Exercise'])] = chest
        wmt_dict['Back'][len(wmt_dict['Exercise'])] = back
        wmt_dict['Legs'][len(wmt_dict['Exercise'])] = legs
        wmt_dict['Core'][len(wmt_dict['Exercise'])] = core
        wmt_dict['Cardio'][len(wmt_dict['Exercise'])] = cardio
        wmt_dict['Favorite'][len(wmt_dict['Exercise'])] = favorite


# In[13]:


addExer('kick_backs', True, False, False, False, False, True, False, False, False)
wmt_dict


# In[14]:


my_prog = {'Date':
               {0: '02/08/2020'},
           'Exercise' : 
               {0: 'pushups'},
           'Sets':
               {0: 3},
           'Reps':
               {0: 15},
           'Weight':
               {0: 0},
           'Speed':
               {0: 0},
           'Distance':
               {0: 0},
            'Duration':
               {0: 0},
           'Difficulty':
               {0: 3},
           'Enjoyability':
               {0: 7}
          }


# In[15]:


my_prog


# In[16]:


#Add Progress Entry to my_prog Dict
def addProg(date, name, sets, reps, weight, speed, distance, duration, difficulty, enjoyability):
    my_prog['Date'][len(my_prog['Enjoyability'])] = date 
    my_prog['Exercise'][len(my_prog['Enjoyability'])] = name
    my_prog['Sets'][len(my_prog['Enjoyability'])] = sets
    my_prog['Reps'][len(my_prog['Enjoyability'])] = reps
    my_prog['Weight'][len(my_prog['Enjoyability'])] = weight
    my_prog['Speed'][len(my_prog['Enjoyability'])] = speed
    my_prog['Distance'][len(my_prog['Enjoyability'])] = distance
    my_prog['Duration'][len(my_prog['Enjoyability'])] = duration
    my_prog['Difficulty'][len(my_prog['Enjoyability'])] = difficulty
    my_prog['Enjoyability'][len(my_prog['Enjoyability'])] = enjoyability


# In[17]:


addProg('02/08/2020', 'treadmill', 0,0,0,0,3, 1, 3, 7)
my_prog


# In[31]:


# function to return key for any value 
def get_key(val): 
    for key, value in my_prog['Exercise'].items(): 
        if val == value:
            return (key) 
  
    print ("key doesn't exist")


# In[32]:


get_key('pushups')


# In[33]:


def diffIncr(exercise):
    if (exercise != Cardio):
        reps = reps * .20
        #count number of entries or weeks of doing exercise
        #increase count times 20% to
        #count number of increments to sets, reps, and weight
        #increase reps first, then increase weight and lower reps back to base
        reps = reps_base
        reps_count += 1
        weight = weight * .20
        weight_count += 1
        
    else:
        distance = my_prog[Distance][1]
        distance = distance * .20
        speed = speed * .20
        #increase distance by increment times 20% first 
        #then maintain speed but increase time/distance
        #alternate
        print (distance)


# In[50]:


def suggestedIncr(exercise):
    if (exercise in my_prog['Exercise']):
        #grab date of most recent entry of that exercise
        #use that index to find the difficulty of that entry
        if (difficulty < 3 & wmt_dict['Cardio'][key==exercise]):
            diffIncr(exercise)
    
    difficulty = my_prog['Difficulty'][get_key(exercise)]
    distance = my_prog['Distance'][get_key(exercise)]
    print("Suggested Distance for next time: " + str(distance * 1.2))
    #difficulty = my_prog[wm]
        


# In[51]:


suggestedIncr('treadmill')


# In[25]:


my_prog['Exercise'][1] = 'treadmill'
my_prog['Exercise'][1]


# In[46]:


my_prog['Difficulty'][1]


# In[47]:


my_prog['Reps'][1]


# In[28]:


my_prog


# In[29]:


#Print Entry in my_prog
def printEntry(locationInteger):
    for item in my_prog:
        print (my_prog[item][locationInteger])


# In[30]:


printEntry(0)


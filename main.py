import json
import random
import slack
import re
from random import sample  

#pip install slack
#pip install slackclient

 
client = slack.WebClient(token="slackToken")
emoji = [":blue_heart:",":green_heart:",":purple_heart:",":fire:",":heartpulse:",":sparkling_heart:",":muscle:",":new_moon:",":volcano:",":ghost:",":confetti_ball:",":crystal_ball:",":globe_with_meridians:",":yellow_heart:",":eyes:"]

def get_type_of_workout():
    samples = []
    f = open('Workout.json')
    data = json.load(f)

    for i in data:
        samples.append(i)
    
    f.close()
    types_of_workout = sample(samples, 5)
    the_workout = get_workouts(types_of_workout)
    reps = workout_reps(types_of_workout, the_workout)
    return types_of_workout, the_workout, reps

def get_workouts(workout):
    the_workout = []
    f = open('Workout.json')
    data = json.load(f)
    for x in range(len(workout)):
        samples = []
        for i in data[workout[x]]:
            samples.append(i)
        
        the_workout += [sample(samples, 5)]
    f.close()
    return the_workout

def workout_reps(workout, the_workout):
    the_reps = []
    f = open('Workout.json')
    data = json.load(f)
    for x in range(len(workout)):
        samples = []
        for i in range(len(the_workout[x])):
            samples.append(sample(data[workout[x]][the_workout[x][i]], 1))
        the_reps += [samples]
    return the_reps     



def get_workout_two(workout,exercises,reps):
    outter = random.choice(emoji)
    for i in range(len(workout)):
        client.chat_postMessage(channel='#climbing-workout-generator', blocks=[
            {
                'type':'section',
                'text':{
                    'type':'mrkdwn',
                    'text':(
                        outter +' *' + workout[i] + '* ' + outter + '\n'
                    )
                }
            }
        ])
        for x in range(len(exercises)):
            char_to_rep = "''"
            pattern = "[" + char_to_rep + "]"
            new_rep = re.sub(pattern, "", str(reps[i][x]))

            client.chat_postMessage(channel='#climbing-workout-generator', blocks=[
            {
                'type':'section',
                'text':{
                    'type':'mrkdwn',
                    'text':(
                        exercises[i][x] + ' : ' + new_rep + '\n'
                    )
                }
            }
        ])






if __name__ == "__main__":
    parsed = get_type_of_workout()
    workout = parsed[0]
    exercises = parsed[1]
    reps = parsed[2]
    get_workout_two(workout, exercises, reps)

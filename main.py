import slack
from workouts_gen import workout_gen, emojis
from re import sub
from time import sleep

client = slack.WebClient(token="slackToken")


def get_workout_two(workout,exercises,reps, emoji):
    for i in range(len(workout)):
        client.chat_postMessage(channel='#climbing-workout-generator', blocks=[
            {
                'type':'section',
                'text':{
                    'type':'mrkdwn',
                    'text':(
                        emoji +' *' + workout[i] + '* ' + emoji + '\n'
                    )
                }
            }
        ])
        for x in range(len(exercises[i])):
            char_to_rep = "''"
            pattern = "[" + char_to_rep + "]"
            new_rep = sub(pattern, "", str(reps[i][x]))
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
            sleep(3)

    client.chat_postMessage(channel='#climbing-workout-generator', blocks=[
            {
                'type':'section',
                'text':{
                    'type':'mrkdwn',
                    'text':(
                        emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji +emoji + emoji + emoji + emoji + emoji+ emoji +emoji + emoji + emoji + emoji + emoji + emoji + '\n' +
                        'END OF EXERCISES FOR THIS WEEK\n' +
                        emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji + emoji +emoji + emoji + emoji + emoji + emoji+ emoji +emoji + emoji + emoji + emoji + emoji+ emoji
                    )
                }
            }
        ])


if __name__ == "__main__":
    wrkGen, emj = workout_gen(), emojis()
    parsed = wrkGen.get_type_of_workout()
    workout, exercises, reps = parsed[0], parsed[1], parsed[2]
    emoji =  emj.emoji_gen()
    get_workout_two(workout, exercises, reps, emoji)

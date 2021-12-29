
from json import load
from random import sample, choice


class workout_gen:
    def get_type_of_workout(self):
        samples = []
        f = open('./json/Workout.json')
        data = load(f)

        for i in data:
            samples.append(i)
        
        f.close()
        types_of_workout = sample(samples, 5)
        the_workout = self.get_workouts(types_of_workout)
        reps = self.workout_reps(types_of_workout, the_workout)
        return types_of_workout, the_workout, reps

    def get_workouts(self, workout):
        the_workout = []
        f = open('./json/Workout.json')
        data = load(f)
        for x in range(len(workout)):
            samples = []
            for i in data[workout[x]]:
                samples.append(i)
            
            the_workout += [sample(samples, 5)]
        f.close()
        return the_workout

    def workout_reps(self, workout, the_workout):
        the_reps = []
        f = open('./json/Workout.json')
        data = load(f)
        for x in range(len(workout)):
            samples = []
            for i in range(len(the_workout[x])):
                samples.append(sample(data[workout[x]][the_workout[x][i]], 1))
            the_reps += [samples]
        return the_reps

class emojis:
    def emoji_gen(self):
        f = open('./json/Emoji.json')
        data = load(f)
        return choice(data["emoji"])
 
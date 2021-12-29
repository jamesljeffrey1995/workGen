# Workout API



## What this app does

Creates a workout plan for the week and then sends that to relevant splunk channel. Use CRON job in gitlab to schedule this everyweek, as this creates a new workout with diffrent reps everytime it runs. To add more workouts, just edit the ***Workout.json*** file, but follow the pattern; this is the same as the ***Emoji.json***.



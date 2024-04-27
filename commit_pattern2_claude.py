import subprocess
import os
from datetime import datetime, timedelta

# Define the pattern (1 for commit, 0 for no commit)
pattern = [
    [0, 1, 0, 1, 0, 1, 0],  # Week 1
    [1, 0, 1, 0, 1, 0, 1],  # Week 2
    [0, 1, 0, 1, 0, 1, 0],  # Week 3
    [1, 0, 1, 0, 1, 0, 1],  # Week 4
    [0, 1, 0, 1, 0, 1, 0],  # Week 5
    [1, 0, 1, 0, 1, 0, 1],  # Week 6
    [0, 1, 0, 1, 0, 1, 0],  # Week 7
]

# Start date (beginning of 2019)
start_date = datetime(2019, 1, 1)

# End date (today)
end_date = datetime.now().date()

# Initialize current date, week index, and day index
current_date = start_date
week_index = 0
day_index = 0

try:
    # Loop until the current date exceeds the end date
    while current_date.date() <= end_date:
        # Check if the pattern indicates a commit for the current day
        if pattern[week_index][day_index] == 1:
            # Format the current date as a string
            date_str = current_date.strftime('%Y-%m-%dT%H:%M:%S')
            print(f'Adding empty commit for date: {date_str}')
            # Set the GIT_COMMITTER_DATE environment variable
            os.environ['GIT_COMMITTER_DATE'] = date_str
            # Run the git commit command with the specified date
            subprocess.run(['git', 'commit', '--allow-empty', '--date', date_str, '-m', f'Empty commit on {date_str}'], check=True)
        
        # Move to the next day
        current_date += timedelta(days=1)
        day_index = (day_index + 1) % 7  # Increment day index and wrap around after 7 days
        if day_index == 0:
            week_index = (week_index + 1) % len(pattern)  # Increment week index and wrap around after the pattern length
            if week_index == 0:
                # Reset the pattern to the beginning if we have completed a full cycle
                week_index = 0

    # Push the commits to the remote repository
    print('Pushing commits to the remote repository...')
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
except subprocess.CalledProcessError as e:
    # Handle errors from subprocess calls
    print(f"An error occurred while running a subprocess: {e}")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")
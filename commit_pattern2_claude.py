import subprocess
import os
from datetime import datetime, timedelta

# Define the pattern (1 for commit, 0 for no commit)
pattern = [
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
]

# Start date (beginning of 2019)
start_date = datetime(2019, 1, 1)

# End date (today)
end_date = datetime.now().date()

# Create commits based on the pattern
current_date = start_date
week_index = 0
day_index = 0

try:
    while current_date.date() <= end_date:
        if pattern[week_index][day_index] == 1:
            date_str = current_date.strftime('%Y-%m-%dT%H:%M:%S')
            print(f'Adding empty commit for date: {date_str}')
            os.environ['GIT_COMMITTER_DATE'] = date_str
            subprocess.run(['git', 'commit', '--allow-empty', '--date', date_str, '-m', f'Empty commit on {date_str}'], check=True)
        
        # Move to the next day
        current_date += timedelta(days=1)
        day_index = (day_index + 1) % 7
        if day_index == 0:
            week_index = (week_index + 1) % len(pattern)
            if week_index == 0:
                # Reset the pattern to the beginning if we have completed a full cycle
                week_index = 0

    # Push the commits to the remote repository
    print('Pushing commits to the remote repository...')
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
except subprocess.CalledProcessError as e:
    print(f"An error occurred while running a subprocess: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
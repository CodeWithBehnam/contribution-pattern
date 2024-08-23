import os
import subprocess
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

# Start date (beginning of August 2023)
start_date = datetime(2023, 8, 1)

# Create commits based on the pattern
for week in range(len(pattern)):
    for day in range(len(pattern[week])):
        if pattern[week][day] == 1:
            date = start_date + timedelta(weeks=week, days=day)
            date_str = date.strftime('%Y-%m-%d')
            with open('README.md', 'a') as file:
                file.write(f'Commit on {date_str}\n')
            print(f'Adding commit for date: {date_str}')
            subprocess.run(['git', 'add', 'README.md'], check=True)
            subprocess.run(['git', 'commit', '--date', date_str, '-m', f'Commit on {date_str}'], check=True)

# Push the commits to the remote repository
print('Pushing commits to the remote repository...')
subprocess.run(['git', 'push', 'origin', 'main'], check=True)
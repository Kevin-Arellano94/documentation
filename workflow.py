# https://raw.githubusercontent.com/Kevin-Arellano94/documentation/main/workflow.py
# https://www.btelligent.com/en/blog/best-practice-working-with-paths-in-python-part-1/

import glob

# Variables that are called
domain = r'https://raw.githubusercontent.com'
user = r'/Kevin-Arellano94'
repo = r'/documentation'
branch = r'/main'

# Paths
my_path = r"C:/Users/kevin/Documents/GitHub/eHawk-Inc"
my_github_path = r"D:\a\documentation-action\documentation-action"

# Gets all the MarkDown files
files = glob.glob(
    # my_path +
    my_github_path +
    '*/**/*.md',
    recursive = True
)

for items in files:
    # Changes the \ to / for the files inside the folder
    new_items = items.replace('\\', '/')

    # For development
    # raw_url = new_items.replace(
    #     f'{ my_path }/documentation',
    #     domain + user + repo + branch
    # )

    # For production
    raw_url = new_items.replace(
        f'{ my_github_path }',
        domain + user + repo + branch
    )

    print(raw_url)


print(f'completed...')

exit(0)

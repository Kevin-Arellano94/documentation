import glob

# Variables that are called
domain = r'https://raw.githubusercontent.com'
user = r'/Kevin-Arellano94'
repo = r'/documentation'
branch = r'/main'

# Paths
my_github_path = r"D:\a\documentation-action\documentation-action"

# Gets all the MarkDown files
files = glob.glob(
    my_path +
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
        r'D:\a\documentation-action\documentation-action',
        domain + user + repo + branch
    )

    print(raw_url)


print(f'completed...')

exit(0)

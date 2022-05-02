import glob

domain = r'https:\\raw.githubusercontent.com'
user = r'\Kevin-Arellano94'
repo = r'\documentation'
branch = r'\main'

my_path = r"D:\a\documentation-action\documentation-action"

files = glob.glob(
    my_path +
    '*/**/*.md',
    recursive = True
)

for items in files:
    raw_url = items.replace(
        r'D:\a\documentation-action\documentation-action',
        domain + user + repo + branch
    )
    print(raw_url)


print(f'completed...')

exit(0)

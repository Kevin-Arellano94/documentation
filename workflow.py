PROD = True

import glob

domain  = r'https://raw.githubusercontent.com'
user    = r'/Kevin-Arellano94'
repo    = r'/documentation'
branch  = r'/main'

if (PROD):
    path = r"D:/a/documentation-action/documentation-action"
else:
    path = r"C:/Users/kevin/Documents/GitHub/eHawk-Inc/documentation"

files = glob.glob(
    path +
    '*/**/*.md',
    recursive = True
)

for items in files:
    new_items = items.replace('\\', '/')

    raw_url = new_items.replace(
        f'{ path }',
        domain + user + repo + branch
    )

    print(raw_url)

print(f'completed...')

exit(0)

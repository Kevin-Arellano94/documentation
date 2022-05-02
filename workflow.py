import glob

my_path = r"D:\a\documentation-action\documentation-action"

files = glob.glob(
    my_path +
    '*/**/*.md',
    recursive = True
)

for items in files:
    print(items)


print(f'completed...')

exit(0)

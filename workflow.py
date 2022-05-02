import glob

# my_path = "C:/Users/kevin/Documents/GitHub/eHawk-Inc"
my_path = "D:/a/documentation-action/documentation-action"

files = glob.glob(
    my_path +
    '*/**/*.md',
    recursive = True
)

print(f'{ files }')
print(f'completed...')

exit(0)

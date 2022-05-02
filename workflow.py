import os
import glob


hw = "Hello World!"
print(hw)

my_path = "/Users/kevin/Documents/GitHub/eHawk-Inc"

files = glob.glob(
    my_path +
    '*/**/*.md',
    recursive = True
)

print(f'{ files }')
print(f'completed...')

exit(0)

from progress.bar import Bar

it = 2000

for i in Bar('Processing').iter(it):
    # Do some work
    pass

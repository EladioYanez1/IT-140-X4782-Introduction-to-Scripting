path = input()
series = {}

# My file is the variable that lets us access the contents of the file, it is the contents of the file.
with open(path, 'r') as myfile:
    # The list of lines.
    readfile = myfile.readlines()
# The first value is start, the second value is the end, and the third is the step.
for i in range(0, len(readfile), 2):
    # This goes over every line from 0 and onwards by a stride of 2.
    num_of_seasons = int(readfile[i].strip('\n'))
    # This goes over every line from 1 and onwards by a stride of 2.
    shows = readfile[i + 1].strip('\n')
    if num_of_seasons in series:
        series[num_of_seasons].append(shows)
    else:
        series[num_of_seasons] = [shows]
# This sorts the items by the key in numerical order. 
sorted_items = sorted(series.items())

# Output is the variable we use to manipulate our output file.
with open('output_keys.txt', 'w') as output:
    # This sets up all the key and value, which we use for this list.
    for key, value in sorted_items:
        
        output.write("{}: {}\n".format(key, "; ".join(value)))
# This is the initial list that we use for just the values of the tv shows.
tv_series = series.values()
# This compiles all the sublist we've made together into a major list and sorts them all. 
sorted_tv_series = sorted([item for sublist in tv_series for item in sublist])
with open('output_titles.txt', 'w') as output:
    for value in sorted_tv_series:
        output.write("{}\n".format("".join(value)))
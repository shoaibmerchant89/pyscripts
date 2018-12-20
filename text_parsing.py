import os
path = os.path.join(os.path.expanduser('~'), 'Desktop')

with open('{0}\\cert_0_site1.lab.com.txt'.format(path)) as f:
    # Skips text before the beginning of the interesting block:
    for line in f:
        if line.strip() == 'BEGIN':  # Or whatever test is needed
            break
        # Reads text until the end of the block:
    for line in input_data:  # This keeps reading the file
        if line.strip() == 'END':
            break
        print line  # Line is extracted (or block_of_lines.append(line), etc.)
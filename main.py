import sys
import os
from config import Config

config=Config()
argument=sys.argv[1:]
files=[]
flags=[]

def handle_input():
    if not argument:
        return False
    seen_file=False
    for arg in argument:
        if arg.startswith("-"):
            if seen_file:
                return False
            flags.append(arg[1:])
        else:
            files.append(arg)
            seen_file=True
            
    return True

def handle_flags():
    if not flags:
        config.line_count=True
        config.word_count=True
        config.byte_count=True
        return
    for flag in flags:      
        for c in flag.lower():
            if c=="l":
                config.line_count=True
            elif c=="w":
                config.word_count=True
            elif c=="c":
                config.byte_count=True
            elif c=="m":
                config.character_count=True
            

def word_count_imp():
    result=[]
    for file in files:
        result.append(process_file(file))
    return result

def process_file(file):
    try:
        with open(file,"r") as f:
            all_lines=f.readlines()
            result_string=[]
            if config.line_count:
                lines=line_counter(all_lines)
                result_string.append(str(lines))
            if config.word_count:
                words=word_counter(all_lines)
                result_string.append(str(words))
            if config.character_count:
                characters=character_counter(all_lines)
                result_string.append(str(characters))
            if config.byte_count:
                byte_count_val=byte_counter(f)
                result_string.append(str(byte_count_val))
            result_string.append(file)
            return [" ".join(result_string), True]
    except FileNotFoundError as not_found:
        return [not_found.filename,False]
  

def line_counter(all_lines):
    # will be implemented if line_count is set to True
    # returns the number of lines
    return len(all_lines)

def word_counter(all_lines):
    # is only called when word_count is set to True
    # returns the number of words
    words=0
    for line in all_lines:
        words+=len(line.split())
    return words

def character_counter(all_lines):
    characters=0
    for line in all_lines:
        characters+=len(line)
    return characters

def byte_counter(file):
    return os.path.getsize(file.name)

def print_result():
    # will need to change the condition for the file not found into something more logical, and indepeneded of the length
    result=word_count_imp()
    for res in result:
        if not res[1]:
            print(res[0]+" was not found")
        else:
            print(res[0])
if __name__=="__main__":
    if not handle_input():
        print("Invalid Input")
        quit()
    handle_flags()
    print_result()

# add a total feature, that adds all the data from the files given
# add a -L flag, for the longest line feature
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
    flags_empty=True
    for arg in argument:
        if arg.startswith("-"):
            flags.append(arg[1:])
            flags_empty=False
        else:
            files.append(arg)
            if flags_empty:
                return False
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
                result.append([" ".join(result_string)])
        except FileNotFoundError as not_found:
            result.append([not_found.filename])
    return result

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
    result=word_count_imp()
    for res in result:
        if len(res[0].split())==1:
            print(f"{res[0]} was not found")
        else:
            print(res[0])
if __name__=="__main__":
    if not handle_input():
        print("Invalid Input")
        quit()
    handle_flags()
    print_result()
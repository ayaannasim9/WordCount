import sys
argument=sys.argv[1:]
files=[]
flags=[]
# print(files)
# flags={
#     'l':"line_count",
#     'w':"word_count",
#     'c':"character_count",
#     'm':"byte_count"
# }
def handle_input():
    if not argument:
        return False
    for arg in argument:
        if arg.startswith("-"):
            flags.append(arg[1:])
        else:
            files.append(arg)
    return True
def word_count():
    result=[]
    for file in files:
        lines=0
        words=0
        characters=0
        try:
            with open(file,"r") as f:
                all_lines=f.readlines()
                for line in all_lines:
                    lines+=1
                    words+=len(line.split())
                    characters+=len(line)
                result.append([f"{lines} {words} {characters} {file}"])
        except FileNotFoundError as not_found:
            result.append([not_found.filename])
    return result
def print_result():
    result=word_count()
    for res in result:
        if len(res[0].split())==1:
            print(f"{res[0]} was not found")
        else:
            print(res[0])
if __name__=="__main__":
    if not handle_input():
        print("You have not entered any file")
        quit()
    print(flags)
    print(files)
    print_result()
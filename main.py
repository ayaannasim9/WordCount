import sys
files=sys.argv[1:]
# print(files)

def handle_input():
    if not files:
        return False
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
            # print(not_found.filename)
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
    print_result()
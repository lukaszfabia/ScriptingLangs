import sys
from Parser import ParseLog
        

def read_log():
    for line in sys.stdin:
        yield ParseLog(line.rstrip()).wrap_log()

def sort_log(key=None):
    logs = list(read_log())
    if key:
        logs.sort(key=key)
    return logs

if __name__ == '__main__':
    sorted_logs = sort_log(key=lambda curr: curr[0])
    for elem in sorted_logs:
        print(elem)
    

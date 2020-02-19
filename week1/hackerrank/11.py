def count_substring(string, sub_string):
    cnt=0
    len_s=len(string)
    len_ss=len(sub_string)
    for i in range(0,len_s):
        tmp=string[i:i+len_ss]
        if(tmp==sub_string):
            cnt=cnt+1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
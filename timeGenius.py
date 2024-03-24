
def solution(T):
    # mod the time in seconds and divide to get to the different "time" categories
    # h = T/(60s*60min) mod 24 to get rest for hours 
    # m = T/60s t get the time in minutes and mod 60 to get rest for min
    # s = T mod 60, since T is already in time 

    s = int(T % 60)
    m = int(round(T/60,0) % 60)
    h = int(round(T/(60*60), 0) % 24)
    return "{}h{}m{}s".format(h,m,s)
    






def main():
    T = 83320
    print(solution(T))


if __name__ == '__main__':
    main()
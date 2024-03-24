
class Solution:
    def sort012(self,arr,n):
        zero=[]
        ones= []
        twos = []

        for el in arr:

            if el == 0:
                zero.append(0)
            elif el == 1:
                ones.append(1)
            elif el == 2:
                twos.append(2)

        arr.clear()
        zero.extend(ones)
        zero.extend(twos)
        arr.extend(zero)

    def smallestInt(self, A):
        maximum = 0
        minimum = 999999999
        array = between
        
            
        pass

        
            



                



def main():
    arr = [0,2,1,2,0]
    ob=Solution()
    ob.sort012(arr, len(arr))
    print(arr)


if __name__ == '__main__':
    main()
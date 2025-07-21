# def squareRoot(lst):
#     resut = {}
#     for num in lst:
#         resut[num] = round(num ** 0.5, 2)
#         return resut
    
def remove(str):
    result = ""
    for char in str:
        if str.count(char) == 1:
            result += char
            return result
        

    
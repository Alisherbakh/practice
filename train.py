# K-TASK (PYTHON)

# Shunday function yozing, u string qabul qilsin va
# string ichidagi eng uzun sozni qaytarsin.
# MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"

def find_longest(a):
    b = a.split(" ")

    return max(b, key=len)


result = find_longest("I come from Uzbekistan")
print("result:", result)


# I-TASK (PYTHON)

# Shunday function tuzing, unga string argument pass bolsin.
# Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
# MASALAN: get_digits("m14i1t") return qiladi "141"
# Yechim :


# def get_num(arg):
#    numb = []
#    for b in arg:
#        if b.isdigit():
#            numb.append(b)
#    return "".join(numb)


# result = get_num("m14i1t")
# print("result:", result)


# G-TASK (PYTHON)

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va
# function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.


# def get_highest(num):
#   a = max(num)
#    b = num.index(a)
#    return f"index:{b}  value:{a}"


# result = get_highest([5, 21, 12, 21, 8])
# print("result:", result)

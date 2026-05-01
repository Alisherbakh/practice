# G-TASK (PYTHON)

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va
# function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.


def get_highest(num):
    a = max(num)
    b = num.index(a)
    return f"index:{b}  value:{a}"


result = get_highest([5, 21, 12, 21, 8])
print("result:", result)

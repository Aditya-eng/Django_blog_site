import re
from pdfminer.high_level import extract_text,extract_pages

text1 = extract_text("answer_key2023.pdf")
text2 = text1.replace(" ","")
text3 = ''.join(text1.split())
# print(text3)
print()
print("---------------------------")
# # print(text1)
# for i in range(16400,16460):
#     print(text3[i],end="")
# print()
# print("----------------------------")

# pattern = re.compile(r"(\w+){0,100}Chosen Option : \d")
# pattern = re.compile(r"Chosen Option : \d")

# print(pattern)
# pattern = re.compile(r"Question ID((.|\n)*)Chosen Option : \d\s")

# pattern = re.compile(r"QuestionID.*ChosenOption:\d")
pattern = re.compile(r"(QuestionID:\d{9}Option1ID:\d{9}Option2ID:\d{9}Option3ID:\d{9}Option4ID:\d{9}Status:(MarkedForReview|Answered)ChosenOption:\d)")
                        #QuestionID:366694273Option1ID:366694819Option2ID:366694822Option3ID:366694821Option4ID:366694820Status:MarkedForReviewChosenOption:4
matches = pattern.findall(text3)

print(len(matches))

print("------------------------")
i1=0
t1 = matches[0][0]
print(t1)
print("------------------------")
x = matches[0][0][-1]# in matches[0][0]<---- second zero is fixed, also [-1] gives the last element
x1 = t1.find("n"+x+"ID:")
s1 = t1[x1+5]
n1=0
m1=[]
a1=""
for i in range(100):
    if n1!=9:
        # m1.append(t1[x1+5+i])
        a1+=str(t1[x1+5+i])

        n1+=1
    else:
        break


print(s1)#first number of optionID
#print(x1)#
print(m1)#list


print(a1)#string with optionID

key = t1[11:20]
# print(t1[11:20])


print("------------------------")
list1 = []

for o1 in range(len(matches)):
    # print(matches[o1][0][-1])
    t11 = matches[o1][0]
    x11 = t11.find("n" + matches[o1][0][-1] + "ID:")
    # s11 = matches[o1][0][x11 + 5]
    n11 = 0
    a11=""
    dict_1 = {}
    for i11 in range(100):
        if n11 != 9:
            # m1.append(t1[x1+5+i])
            a11 += str(t11[x11 + 5 + i11])

            n11 += 1
        else:
            break
        # print(t11[11:20]," ",a11)
    dict_1.update({t11[11:20]:a11})
    list1.append(dict_1)

    # print(dict_1)


print(len(list1))


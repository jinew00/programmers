# 소문자 문자열로부터 자음 서브문자(consonant substrings)의 최
# 대합을 구하는 프로그램을 구현하세요. (4점)
# – solve(문자열) 함수
# – 입력된 문자열은 소문자이고, 문자간에 공백이 없다.
# – 문자열에서 모음(aeiou)은 제외한다.
# – 알파벳 값은 a = 1, b = 2, c = 3, .... z = 26
# • 예)
# solve("zodiacs") 일 때 반환 값은 26
# • "zodiacs"에서 모음(o,ia)을 뺀 자음은 “z d cs"
# • 자음은 ＂z＂, ＂d＂와 "cs“ 이고, z = 26, d = 4와 cs = 3 + 19 = 22를 가
# 진다. 여기서 최대 값은 26
# • 반환 값 26
# solve("strength") 일 때 반환 값은 57
# • 자음은 "str" and "ngth＂이고, 자음이 연속일 때 전체 합으로 표현한다.
# • "str" = 19 + 20 + 18 = 57이고, ＂ngth＂ = 14 + 7 + 20 + 8 = 49이다. 


import re
def solve(string):
    sum=0
    summ=[]
    
    ja={'a':0, 'b':2, 'c':3, 'd':4,'e':0, 'f':6,'g':7,'h':8,'i':0,'j':10,'k':11,'l':12,'m':13,'n':14,'o':0,'p':16,'q':17,'r':18,'s':19,'t':20,'u':0,'v':22,'w':23,'x':24,'y':25,'z':26}
    
    substr=re.split('a|e|i|o|u', string)
    
    for i in range(0,len(substr)):
        
        for a in substr[i]:
            sum=sum+ja[a]
            print(substr[i], a,ja[a],"  ",sum)
            summ.insert(i,sum)
        sum=0
    
    summ.sort(reverse=True)
    return summ[0]
print(solve('zodiacs'))
print(solve('strength'))




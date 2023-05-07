# 두개의 리스트를 입력 받아 A-B를 빼는 프로그램을 구현하세요.
# (4점)
# – array_diff(A,B) 함수
# • 예
# array_diff([1,2],[1])
# • 여기서 list A=[1,2]이고, list B=[1]이다.
# • A-B를 통해 반환 [2]를 반환한다.
# array_diff([1,2,2,2,3],[2]) 일 때 반환 값 [1,3]
# array_diff([1,2,2], [1]) 일 때 반환 값 [2,2]
# array_diff([1,2,2], []) 일 때 반환 값 [1,2,2]
# array_diff([], [1,2]) 일 때 반환 값 []

def array_diff(A,B):
    an=[]
    for i in A:
        for a in B:
            if i!=a:
                an.append(i)
    return an
print(array_diff([1,2,2,2,3],[2]))
print(array_diff([1,2,2,2,3],[]))
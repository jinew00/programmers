# 4. 문자열로 주어진 URL 주소 정보로부터 도메인 이름을 반환하는 프
# 로그램을 구현하세요. (4점)
# – domain_name(string) 함수
# • 예)
# domain_name(“http://github.com/carbonfive/raygun”) == "github"
# domain_name("www.google.com") == “google"
# domain_name("https://www.netflix.com") == “netflix"

def domain_name(string):
    string=string.replace('http://','')
    string=string.replace('https://','')
    string=string.replace('www.','')
    string=string.split('.')
    
    print (string[0])


domain_name('http://github.com/carbonfive/raygun')
domain_name('www.google.com') 
domain_name('https://www.netflix.com')
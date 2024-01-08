import random
def join_demo():
    footballteam = ('mun','liv','man','ars','wes','che','juv','psg','bar','mad','wol','bar')
    print(footballteam)
    print(" ".join(footballteam))

def password_gen(length):
    s = list("fiojwefgbjkwerabhjklsg312894879023567842")
    #print(s,"\n")
    p = random.sample(s, length)
    #print(p)
    return "".join(p)
def replace():
    s = 'password'
    s1 = s.replace('a','@')
    s2 = s.replace('a','@').replace('r','R')
    s3 = s.replace('pass','fail')
    print(s,s1,s2,s3)
#join_demo()
# for n in range(10):
#     print(password_gen(5))

replace()
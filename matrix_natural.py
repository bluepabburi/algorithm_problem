def solution(n):
    ans = []
    sen = str(n)
    

    for i in range(len(sen)):
        
        ans.insert(0,int(sen[i]))
    
    print(ans)
    
    return ans


solution(12345)


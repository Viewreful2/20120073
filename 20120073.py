t = int(input())
board= [[ 0 for j in range(5)] for i in range(0,5)]

for test in range(0,t):
    for j in range(0,5):
    
        board[j]=list(map(int, input().split()))
        
    number=list(map(int, input().split()))
    
    for a in range(len(number)):
        flag = False
        
        for j in range(0,5):
            for i in range(0,5):
                if(board[j][i] == number[a]):
                    board[j][i] = 0
                    flag = True
                    break
                    
            if(flag == True):
                break
                
        if(flag == True) :
            if(board[4][4] + board[4][0] + board[0][4] + board[0][0] == 0 ): 
                print(a+1)
                break
            if(board[4][0] + board[3][1] + board[2][2] + board[1][3] + board[0][4] == 0 ):
                print(a+1)
                break    
            if(board[4][4] + board[3][3] + board[2][2] + board[1][1] + board[0][0] == 0 ):
                print(a+1)
                break    
            
            flag = False
            for j in range(0,5) :
                if(board[j][0] + board[j][1] + board[j][2] + board[j][3] + board[j][4] == 0 ):
                    print(a+1)
                    flag = True
                    break
                if(board[0][j] + board[1][j] + board[2][j] + board[3][j] + board[4][j] == 0 ):
                    print(a+1)
                    flag = True
                    break
                    
            if(flag == True): 
                break

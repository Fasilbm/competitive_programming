class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players=[]
        for i in range(1,n+1):
            players.append(i)
        index=0
        while len(players)>1:
            index=(index+k-1)%len(players)
            players.remove(players[index])
        return players[0]

    

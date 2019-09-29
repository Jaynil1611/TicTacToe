# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 08:18:38 2019

@author: Jaynil Gaglani
"""
import os
import sys
game=[" "," "," "," "," "," "," "," "," "]
#game list starts with index 0 so game[n-1] will be used when the list is checked for block or insert


def print_game():
    os.system('cls')
    print(" "+game[0]+"| "+game[1]+"| "+game[2])
    print("__|__|__")
    print(" "+game[3]+"| "+game[4]+"| "+game[5])
    print("__|__|__")    
    print(" "+game[6]+"| "+game[7]+"| "+game[8])


def player(p):
    print("Choose an empty space from 1-9 : ")
    t=int(input())
    if(game[t-1]!=" "):
        print("Space not empty ")
        player(p)
    else:
        game[t-1]=p
    print_game()
        
def check_result(p1,p2):
#    Set() is data structure which contain only unique values and " " are not well dealt in set.It needs values
#    range(8) will iterate till 7
    value=9
    for i in range(9):
        if(game[i]==" "):
            game[i]=value
            
    solution1=list(set((game[0],game[4],game[8])))
    solution2=list(set((game[0],game[1],game[2])))
    solution3=list(set((game[3],game[4],game[5])))
    solution4=list(set((game[6],game[7],game[8])))
    solution5=list(set((game[0],game[3],game[6])))
    solution6=list(set((game[1],game[4],game[7])))
    solution7=list(set((game[2],game[5],game[8])))
    solution8=list(set((game[6],game[7],game[8])))
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]
    
    for i in range(8):
        if(len(result[i])==1 and result[i][0]!=9):
            if result[i][0]==p1:
                print("Player 1 wins the game ")
            else:
                print("Player 2 wins the game ")
            value=5
    for i in range(9):
        if(game[i]==9):
            game[i]=" "
    if(value==5):
        return 1
    return 0
#    If len(result[i])==1 means inner list of solution is of length 1 and result[i][0]!=6 means 
#    the set of solution contains 
def begin():
    n=0
    print("Press 1> Player 1 = 'X' and Player 2 = '0' \n\t 2> Player 1 = '0' and Player 2 = 'X'")
    tr=int(input())
    count=0
    if tr==1:
        player1='X'
        player2='0'
    else:
        player1='0'
        player2='X'
    while True:
        count+=1
        if(count>9):
            print("Game Drawn ")
            break
        print("Player1's turn :")
        player(player1)
        n=check_result(player1,player2)
        if n==1:
            sys.exit()
        print("Player2's turn :")
        player(player2)
        n=check_result(player1,player2)
        if n==1:
            sys.exit()

#print("   |   |   ")
print("The pattern of tic tac toe board is as follows : ")
print(" 1 | 2 | 3 ")
print("___|___|___")
print(" 4 | 5 | 6 ")
print("___|___|___")
print(" 7 | 8 | 9 ")
#print("   |   |   ")
begin()

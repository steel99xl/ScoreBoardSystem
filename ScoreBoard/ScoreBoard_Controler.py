import os
import re
global BOARD
global current_score

while True:
    def ADD():
        board,score = BOARD.split('|')
        score = score[0:3]
        if(":" in BOARD):
            board,team = BOARD.split(':')
        else:
            team = "null"    
        if(team != "null"):
            f = open(team + ".txt")
            current_score = f.read()
            current_score,current = current_score.split("|")
            if(current_score != ""):
                score = int(score) + int(current)
                f.close
            else:
                f.close
            f = open(team + ".txt","w+")
            f.write(team + "|" + str(score) + "\n")
            f.close
        else:
            pass

    def RMV():
        board,score = BOARD.split('|')
        score = score[0:3]
        if(":" in BOARD):
            board,team = BOARD.split(':')
        else:
            team = "null"
        if(team != "null"):
            f = open(team + ".txt")
            current_score = f.read()
            current_score,current = current_score.split("|")
            if(current_score != ""):
                score = int(current) - int(score)
                f.close
            else:
                f.close
                pass
            f = open(team + ".txt","w+")
            f.write(team + "|" + str(score) + "\n")
            f.close
        else:
            pass

    def NEW():
        baord,team = BOARD.split('=')
        if(team != "" or team != " "):
            os.system("touch " + team +".txt")
            f = open(team + ".txt","w+")
            f.write(team + "|0" + "\n")
            f.close
        else:
            pass
    def DEL():
        baord,team = BOARD.split('=')
        if(team != "" or team != " "):
            os.system("rm " + team + ".txt")
        else:
            pass
    def TEAM():
        baord,team = BOARD.split("|")
        if(team == "TEAMS"):
            os.system("cat TABLE/TABLE.txt")
        else:
            pass
    def HELP():
        print("""
        There are 5 total commands in the controle system
        ADD - adds point to a team
            example - add|300:team
                must use 3 digets 100 010 001
        RMV - removes points from a team
            example - rmv|300:team
                must use 3 digests 100 010 001
        NEW - adds a team with score of 0
            example - new|team=new_team
        DEL - removes a team from list
            example - del|team=new_team
            """)


    def main():
        global BOARD
        BOARD = input("Shell > ")
        BOARD = BOARD.upper()
        if("ADD" in BOARD):
            ADD()
        elif("RMV" in BOARD):
            RMV()
        elif("NEW" in BOARD):
            NEW()
        elif("DEL" in BOARD):
            DEL()
        elif("LIST" in BOARD):
            TEAM()
        elif("HELP" in BOARD):
            HELP()
        else:
            print("Please enter a valid controle option")
    main()

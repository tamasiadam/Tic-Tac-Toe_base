import random #line:1
from menu import get_menu_option #line:2
class TicTacToe :#line:4
    def __init__ (OOO00OO0OOOO0000O ):#line:5
        OOO00OO0OOOO0000O .board =[' 'for _O0O00OOOOOOOOO0OO in range (9 )]#line:6
        OOO00OO0OOOO0000O .current_player ='X'#line:7
    def display_board (OO00OO000O0O00000 ):#line:9
        print ("\n  A   B   C")#line:10
        for OO00O0O0O00O00O0O in range (3 ):#line:11
            O0OOO00O0000OO0OO =OO00OO000O0O00000 .board [OO00O0O0O00O00O0O *3 :(OO00O0O0O00O00O0O +1 )*3 ]#line:12
            print (f"{OO00O0O0O00O00O0O} "+' | '.join (O0OOO00O0000OO0OO ))#line:13
            if OO00O0O0O00O00O0O <2 :#line:14
                print (" ---+---+---")#line:15
        print ("\n")#line:16
    def make_move (O00OO0OOO000OOO0O ,O0O0OO0OOOOOOO0OO ,O0OO00O0OOOO00000 ):#line:18
        OOO0O0OO00OOO000O =O0O0OO0OOOOOOO0OO *3 +O0OO00O0OOOO00000 #line:19
        if 0 <=OOO0O0OO00OOO000O <9 and O00OO0OOO000OOO0O .board [OOO0O0OO00OOO000O ]==' ':#line:20
            O00OO0OOO000OOO0O .board [OOO0O0OO00OOO000O ]=O00OO0OOO000OOO0O .current_player #line:21
            return True #line:22
        return False #line:23
    def check_winner (OOOO000OO00OOO0O0 ):#line:25
        OO0OO0O00OO00O000 =[(0 ,1 ,2 ),(3 ,4 ,5 ),(6 ,7 ,8 ),(0 ,3 ,6 ),(1 ,4 ,7 ),(2 ,5 ,8 ),(0 ,4 ,8 ),(2 ,4 ,6 )]#line:30
        for OO00O000O0O0000O0 ,OO00O0000OO0O0OO0 ,OO00O000O0OOOO0O0 in OO0OO0O00OO00O000 :#line:31
            if OOOO000OO00OOO0O0 .board [OO00O000O0O0000O0 ]==OOOO000OO00OOO0O0 .board [OO00O0000OO0O0OO0 ]==OOOO000OO00OOO0O0 .board [OO00O000O0OOOO0O0 ]!=' ':#line:32
                return OOOO000OO00OOO0O0 .board [OO00O000O0O0000O0 ]#line:33
        return None #line:34
    def is_draw (O0O00O0OOO0OO0O00 ):#line:36
        return all (O0OO000OOO00OO0O0 !=' 'for O0OO000OOO00OO0O0 in O0O00O0OOO0OO0O00 .board )and O0O00O0OOO0OO0O00 .check_winner ()is None #line:37
    def switch_player (OO0OOOOO00OO00OOO ):#line:39
        OO0OOOOO00OO00OOO .current_player ='O'if OO0OOOOO00OO00OOO .current_player =='X'else 'X'#line:40
    def play (OOO0OO00O0O0O0O0O ,O000O00000OOOOOOO ):#line:42
        while True :#line:43
            OOO0OO00O0O0O0O0O .display_board ()#line:44
            print (f"Player {OOO0OO00O0O0O0O0O.current_player}, enter your move (e.g. A0): ",end ='')#line:45
            O0OOOOOO0OO000O0O =input ().strip ().upper ()#line:46
            if len (O0OOOOOO0OO000O0O )!=2 or O0OOOOOO0OO000O0O [0 ]not in 'ABC'or O0OOOOOO0OO000O0O [1 ]not in '012':#line:48
                print ("Invalid input. Use format A0, B1, C2 etc.")#line:49
                continue #line:50
            O0OO000OOOO00000O =ord (O0OOOOOO0OO000O0O [0 ])-ord ('A')#line:51
            OOOOO0O0O000OO0OO =int (O0OOOOOO0OO000O0O [1 ])#line:52
            if not OOO0OO00O0O0O0O0O .make_move (OOOOO0O0O000OO0OO ,O0OO000OOOO00000O ):#line:54
                print ("Cell already taken or invalid. Try again.")#line:55
                continue #line:56
            OO00OOO0OO000O000 =OOO0OO00O0O0O0O0O .check_winner ()#line:58
            if OO00OOO0OO000O000 :#line:59
                OOO0OO00O0O0O0O0O .display_board ()#line:60
                print (f"Congratulations! Player {OO00OOO0OO000O000} wins!")#line:61
                break #line:62
            if OOO0OO00O0O0O0O0O .is_draw ():#line:64
                OOO0OO00O0O0O0O0O .display_board ()#line:65
                print ("It's a draw!")#line:66
                break #line:67
            OOO0OO00O0O0O0O0O .switch_player ()#line:69
    def AI_mode (grid =None ):#line:71
        if grid is None :#line:72
            grid =[" "]*9 #line:73
        def O0O00O0000O0O0O00 ():#line:75
            print (f"{grid[0]}|{grid[1]}|{grid[2]}")#line:76
            print ("-+-+-")#line:77
            print (f"{grid[3]}|{grid[4]}|{grid[5]}")#line:78
            print ("-+-+-")#line:79
            print (f"{grid[6]}|{grid[7]}|{grid[8]}\n")#line:80
        def OOOO0O0OO00O0O00O (O0O0O0OO0OOO000O0 ):#line:82
            O0O000OOO000O00OO =[(0 ,1 ,2 ),(3 ,4 ,5 ),(6 ,7 ,8 ),(0 ,3 ,6 ),(1 ,4 ,7 ),(2 ,5 ,8 ),(0 ,4 ,8 ),(2 ,4 ,6 )]#line:85
            return any (grid [OOO0O00OO00OO0OOO ]==grid [OO0000000OO0O00O0 ]==grid [O0000OO0O00OOO0O0 ]==O0O0O0OO0OOO000O0 for OOO0O00OO00OO0OOO ,OO0000000OO0O00O0 ,O0000OO0O00OOO0O0 in O0O000OOO000O00OO )#line:86
        def O00O0OOOO00000O00 ():#line:88
            return all (O0O0O000O0OOOOO00 !=" "for O0O0O000O0OOOOO00 in grid )#line:89
        def O0OOOO0OO00O00OOO (O0O00OO000O00OO00 ,O00000OOO0O00OO00 ,O0OO0O0000OOO0O0O ,O00O0OO00O000000O ):#line:91
            if OOOO0O0OO00O0O00O (O0O00OO000O00OO00 ):#line:92
                return 1 #line:93
            if OOOO0O0OO00O0O00O (O00000OOO0O00OO00 ):#line:94
                return -1 #line:95
            if O00O0OOOO00000O00 ():#line:96
                return 0 #line:97
            if O00O0OO00O000000O :#line:99
                O0OOOO0OOOOOOO0O0 =-float ("inf")#line:100
                for O0OOO00OOO00O0OO0 in range (9 ):#line:101
                    if grid [O0OOO00OOO00O0OO0 ]==" ":#line:102
                        grid [O0OOO00OOO00O0OO0 ]=O0O00OO000O00OO00 #line:103
                        OOOOOOO000OOOOOO0 =O0OOOO0OO00O00OOO (O0O00OO000O00OO00 ,O00000OOO0O00OO00 ,O0OO0O0000OOO0O0O +1 ,False )#line:104
                        grid [O0OOO00OOO00O0OO0 ]=" "#line:105
                        O0OOOO0OOOOOOO0O0 =max (O0OOOO0OOOOOOO0O0 ,OOOOOOO000OOOOOO0 )#line:106
                return O0OOOO0OOOOOOO0O0 #line:107
            else :#line:108
                O0OOOO0OOOOOOO0O0 =float ("inf")#line:109
                for O0OOO00OOO00O0OO0 in range (9 ):#line:110
                    if grid [O0OOO00OOO00O0OO0 ]==" ":#line:111
                        grid [O0OOO00OOO00O0OO0 ]=O00000OOO0O00OO00 #line:112
                        OOOOOOO000OOOOOO0 =O0OOOO0OO00O00OOO (O0O00OO000O00OO00 ,O00000OOO0O00OO00 ,O0OO0O0000OOO0O0O +1 ,True )#line:113
                        grid [O0OOO00OOO00O0OO0 ]=" "#line:114
                        O0OOOO0OOOOOOO0O0 =min (O0OOOO0OOOOOOO0O0 ,OOOOOOO000OOOOOO0 )#line:115
                return O0OOOO0OOOOOOO0O0 #line:116
        def O0000000000O00O0O (O00O00OO0O0O00OOO ,OOOOO00OOO00O0O00 ):#line:118
            O0O0000000OOOO0OO =-float ("inf")#line:119
            OOO0000OOOOOO0OO0 =None #line:120
            for O000000OO0OO0OO00 in range (9 ):#line:121
                if grid [O000000OO0OO0OO00 ]==" ":#line:122
                    grid [O000000OO0OO0OO00 ]=O00O00OO0O0O00OOO #line:123
                    O0O000OO0OO00O0O0 =O0OOOO0OO00O00OOO (O00O00OO0O0O00OOO ,OOOOO00OOO00O0O00 ,0 ,False )#line:124
                    grid [O000000OO0OO0OO00 ]=" "#line:125
                    if O0O000OO0OO00O0O0 >O0O0000000OOOO0OO :#line:126
                        O0O0000000OOOO0OO ,OOO0000OOOOOO0OO0 =O0O000OO0OO00O0O0 ,O000000OO0OO0OO00 #line:127
            grid [OOO0000OOOOOO0OO0 ]=O00O00OO0O0O00OOO #line:129
            O0O00O0000O0O0O00 ()#line:130
        OO0000OOOO0OOOO0O ,OO0OOOO0OOO0OO000 ="X","O"#line:133
        OO0O0OOO00OO00OOO =random .choice ([OO0000OOOO0OOOO0O ,OO0OOOO0OOO0OO000 ])#line:135
        print (f"Első lép: {OO0O0OOO00OO00OOO}\n")#line:137
        O0O00O0000O0O0O00 ()#line:138
        while True :#line:141
            if OO0O0OOO00OO00OOO ==OO0000OOOO0OOOO0O :#line:142
                O0000000000O00O0O (OO0000OOOO0OOOO0O ,OO0OOOO0OOO0OO000 )#line:143
                if OOOO0O0OO00O0O00O (OO0000OOOO0OOOO0O ):#line:144
                    print ("X won!")#line:145
                    break #line:146
                OO0O0OOO00OO00OOO =OO0OOOO0OOO0OO000 #line:147
            else :#line:148
                O0000000000O00O0O (OO0OOOO0OOO0OO000 ,OO0000OOOO0OOOO0O )#line:149
                if OOOO0O0OO00O0O00O (OO0OOOO0OOO0OO000 ):#line:150
                    print ("O won!")#line:151
                    break #line:152
                OO0O0OOO00OO00OOO =OO0000OOOO0OOOO0O #line:153
            if O00O0OOOO00000O00 ():#line:155
                print ("It's a Draw!")#line:156
                break #line:157
    if __name__ =="__main__":#line:159
        AI_mode ()
import random,getopt
import sys

# Source: https://github.com/pradeep1288/tambola.py
class Generator:
    def __init__(self):
        self.total_tickets = 1
        self.row = 3
        self.column = 9
        self.range = [0,0,0,0,0,0,0,0,0]
    
    def generate(self):
        self.range = [0,0,0,0,0,0,0,0,0]
        ticket_page = {}
        count = 1
        max_num = 27
        j = 1
        ticket = {}
        while j <= max_num:
            rand_num = random.randrange(1,91)
            if rand_num in ticket:
                continue
            else:
                if rand_num < 10 and self.range[0] < 3:
                    ticket[rand_num] = 1
                    self.range[0] = self.range[0] + 1
                    j = j + 1
                elif (rand_num < 20 and rand_num >= 10) and self.range[1] < 3:
                    ticket[rand_num] = 1
                    self.range[1] = self.range[1] + 1
                    j = j + 1
                elif (rand_num < 30 and rand_num >=20) and self.range[2] < 3:
                    ticket[rand_num] = 1
                    self.range[2] = self.range[2] + 1
                    j = j + 1
                elif (rand_num < 40 and rand_num >= 30) and self.range[3] < 3:
                    ticket[rand_num] = 1
                    self.range[3] = self.range[3] + 1
                    j = j + 1
                elif (rand_num < 50 and rand_num >= 40) and self.range[4] < 3:
                    ticket[rand_num] = 1
                    self.range[4] = self.range[4] + 1
                    j = j + 1
                elif (rand_num < 60 and rand_num >= 50) and self.range[5] < 3:
                    ticket[rand_num] = 1
                    self.range[5] = self.range[5] + 1
                    j = j + 1
                elif (rand_num < 70 and rand_num >= 60) and self.range[6] < 3:
                    ticket[rand_num] = 1
                    self.range[6] = self.range[6] + 1
                    j = j + 1
                elif (rand_num < 80 and rand_num >= 70) and self.range[7] < 3:
                    ticket[rand_num] = 1
                    self.range[7] = self.range[7] + 1
                    j = j + 1
                elif (rand_num <=90 and rand_num >= 80) and self.range[8] < 3:
                    ticket[rand_num] = 1
                    self.range[8] = self.range[8] + 1
                    j = j + 1
                else:
                    continue
        ticket_page[str(count)]=list(ticket.keys())
        return ticket_page
    
    def get_ticket(self):
        numbers = self.generate()
        for keys,value in numbers.items():
            row1 = [" "," "," "," "," "," "," "," "," "]
            row2 = [" "," "," "," "," "," "," "," "," "]    
            row3 = [" "," "," "," "," "," "," "," "," "]
            data = (row1,row2,row3)
            j = 0
            count1 = 0
            count2 = 0
            count3 = 0
            for i in range(len(value)):
                rem = int(value[i]/10)
                str_val = str(list(value)[i])
                if rem == 0:
                    if data[j][0] == " " and count1 < 9:
                        data[j][0] = str_val
                        count1 = count1 + 1
                    elif data[j+1][0] == " " and count2 < 9:
                        data[j+1][0] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][0] = str_val
                elif rem == 1:
                    if data[j][1] == " " and count1 < 9:
                        data[j][1] = str_val
                        count1 = count1 + 1
                    elif data[j+1][1] == " " and count2 < 9:
                        data[j+1][1] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][1] = str_val
                elif rem == 2:
                    if data[j][2] == " " and count1 < 9:
                        data[j][2] = str_val
                        count1 = count1 + 1
                    elif data[j+1][2] == " " and count2 < 9:
                        data[j+1][2] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][2] = str_val
                elif rem == 3:
                    if data[j][3] == " " and count1 < 9:
                        data[j][3] = str_val
                        count1 = count1 + 1
                    elif data[j+1][3] == " " and count2 < 9:
                        data[j+1][3] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][3] = str_val
                elif rem == 4:
                    if data[j][4] == " " and count1 < 9:
                        data[j][4] = str_val
                        count1 = count1 + 1
                    elif data[j+1][4] == " " and count2 < 9:
                        data[j+1][4] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][4] = str_val
                elif rem == 5:
                    if data[j][5] == " " and count1 < 9:
                        data[j][5] = str_val
                        count1 = count1 + 1
                    elif data[j+1][5] == " " and count2 < 9:
                        data[j+1][5] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][5] = str_val
                elif rem == 6:
                    if data[j][6] == " " and count1 < 9:
                        data[j][6] = str_val
                        count1 = count1 + 1
                    elif data[j+1][6] == " " and count2 < 9:
                        data[j+1][6] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][6] = str_val 
                elif rem == 7:
                    if data[j][7] == " " and count1 < 9:
                        data[j][7] = str_val
                        count1 = count1 + 1
                    elif data[j+1][7] == " " and count2 <9:
                        data[j+1][7] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][7] = str_val           
                elif rem == 8 or rem == 9:
                    if data[j][8] == " " and count1 < 9:
                        data[j][8] = str_val
                        count1 = count1 + 1
                    elif data[j+1][8] == " " and count2 < 9:
                        data[j+1][8] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][8] = str_val        
                else:
                    print("Hi")    
                    
            print("\n")
        count = 1
        row1_elim = [0,0,0,0,0,0,0,0,0]
        while count <= 4:
            rand_num = random.randrange(0,9)
            if row1_elim[rand_num] != 0:
                continue
            else:
                row1_elim[rand_num] = 1
                count = count + 1
        row3_elim = [0,0,0,0,0,0,0,0,0]
        count = 1 
        while count <= 4:
            rand_num = random.randrange(0,9)
            if row3_elim[rand_num] != 0:
                continue
            else:
                row3_elim[rand_num] = 1
                count = count + 1
        for i in range(0,9):
            if row1_elim[i] == 1:
                data[0][i] = "-"
            else:
                row2_res = i
        row1_elim[row2_res] = 1
        for i in range(0,9):
            if row1_elim[i] == 0:
                data[1][i] = "-"
        for j in range(0,9):
            if row3_elim[j] == 1:
                data[2][j] = "-"
        return data
        

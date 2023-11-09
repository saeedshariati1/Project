import random
import math
import queue
import array

S_i = 0
temp_i = 0
next_clock = 0
S_i2 = 0
S_i3 = 0
w_time_1 = 0
w_time_2 = 0
w_time_3 = 0
#--------------------------------------------------
def genExp(landa): # genExp(1) and genExp(2) and genExp(3) and genExp(4)
    if (landa == 0):
        return 0;
    while (True):
        r = round(random.uniform(0, 1), 3)
        if (r == 0):
            continue
        else:
            temp = round((-1 / landa * math.log(r, 2)), 3)
            if (landa == 2):
                global S_i
                global temp_i
                temp_i = temp
                S_i = round(S_i + temp, 3)
            # return temp
            return temp
def genUniform(start, stop):
   temp = round(random.uniform(0, 1), 1)
   if temp >= 0.4:
        global S_i2
        S_i2 = round(S_i2 + temp, 3)
   if temp <= 0.4:
        global S_i3
        S_i3 = round(S_i3 + temp, 3)
   return temp

#---------------------------------------- #
initialization_time = 0 # T_0 = 0
#---------------------------------------- # system state
server_status = 0
time_of_arrival = queue.Queue()
number_in_queue = time_of_arrival.qsize() # = 0
#---------------------------------------- #
clock = 0
event_list = [0, 0]
#---------------------------------------- # statistical counters
number_serviced = 0
total_delay = 0
area_under_q_t = 0
area_under_b_t = 0
#---------------------------------------- # myself parameters
T_0 = 0 # initialization_time

T_i = 0
A_i = 0

D_i = 0
S_i = 0
C_i = D_i + S_i
#---------------------------------------- # second queue
probability2 = 0
first_time2 = 0
first_time_flag2 = True
#----------------------------------------
server_status2 = 0
time_of_arrival2 = queue.Queue()
number_in_queue2 = time_of_arrival2.qsize() # = 0
#----------------------------------------
clock2 = 0
event_list2 = [0, 0]
#----------------------------------------
number_serviced2 = 0
total_delay2 = 0
area_under_q_t2 = 0
area_under_b_t2 = 0
#----------------------------------------
T_02 = 0 # initialization_time

T_i2 = 0
A_i2 = 0

D_i2 = 0
S_i2 = 0
C_i2 = D_i2 + S_i2
#---------------------------------------- Third queue
probability3 = 0
first_time3 = 0
first_time_flag3 = True
#----------------------------------------
server_status3 = 0
time_of_arrival3 = queue.Queue()
number_in_queue3 = time_of_arrival3.qsize() # = 0
#----------------------------------------
clock3 = 0
event_list3 = [0, 0]
#----------------------------------------
number_serviced3 = 0
total_delay3 = 0
area_under_q_t3 = 0
area_under_b_t3 = 0
#----------------------------------------
T_03 = 0 # initialization_time

T_i3 = 0
A_i3 = 0

D_i3 = 0
S_i3 = 0
C_i3 = D_i3 + S_i3
#----------------------------------------
def initialization():
    # A
    global T_i
    global C_i
    T_i = round(event_list[0] + genExp(1), 3)
    C_i = 99999
    # B
    global server_status
    global number_in_queue
    server_status = 0
    # no put, get
    number_in_queue = time_of_arrival.qsize()  # = 0
    # C
    global clock
    clock = 0
    event_list[0] = T_i
    event_list[1] = C_i
    # D
    global number_serviced
    global total_delay
    global area_under_q_t
    global area_under_b_t
    number_serviced = 0
    total_delay = 0
    area_under_q_t = 0
    area_under_b_t = 0

def second_queue_turn(next_clock):
    if (time_of_arrival2.qsize() != 0):
        while (time_of_arrival2.queue[0][2] < next_clock):
            temp3 = time_of_arrival2.get()  # get out, your service is done.
            global w_time_2
            global area_under_b_t2
            global server_status2
            global number_in_queue2
            global number_serviced2
            global total_delay2

            w_time_2 = round(w_time_2 + (temp3[2] - temp3[0]), 3)

            area_under_b_t2 = round(area_under_b_t2 + (temp3[2] - temp3[0]) - temp3[1], 3)

            server_status2 = 1

            number_in_queue2 = time_of_arrival2.qsize() - 1

            number_serviced2 = number_serviced2 + 1  # number_serviced + 1, because service for 1 customer is done.

            total_delay2 = round(temp3[1] + total_delay2, 3)

            if time_of_arrival2.qsize() == 0:
                break

def third_queue_turn(next_clock):
    if (time_of_arrival3.qsize() != 0):
        while (time_of_arrival3.queue[0][2] < next_clock):
            temp3 = time_of_arrival3.get()  # get out, your service is done.
            global w_time_3
            global area_under_b_t3
            global server_status3
            global number_in_queue3
            global number_serviced3
            global total_delay3

            w_time_3 = round(w_time_3 + (temp3[2] - temp3[0]), 3)

            area_under_b_t3 = round(area_under_b_t3 + (temp3[2] - temp3[0]) - temp3[1], 3)

            server_status3 = 1

            number_in_queue3 = time_of_arrival3.qsize() - 1

            number_serviced3 = number_serviced3 + 1  # number_serviced + 1, because service for 1 customer is done.

            total_delay3 = round(temp3[1] + total_delay3, 3)

            if time_of_arrival3.qsize() == 0:
                break

def findmin(event_list):
    index_min = min(range(len(event_list)), key=event_list.__getitem__)
    return index_min
#-------------------------------------------------------------------------------------------------------------------------

initialization()
run = int(input("Enter number serviced : "))
while (number_serviced < run): # < 1 means service is done for 1 customer.
    if (findmin(event_list) == 0 and event_list[1] == 99999): # from 99999 to 0 | from empty queue to 0
        # A
        T_i = round(event_list[0] + genExp(1), 3)
        C_i = round(event_list[0] + 0 + genExp(2), 3)# D_i = 0
        # B
        server_status = 1
        time_of_arrival.put(event_list[0])
        number_in_queue = time_of_arrival.qsize() - 1
        # C
        clock = event_list[0]
        event_list[0] = T_i
        event_list[1] = C_i
        # D
        # no need for number_serviced
        # no need for total_delay
        # no need for area_under_q_t
        # no need for area_under_b_t
        next_clock = event_list[findmin(event_list)]
        second_queue_turn(next_clock)
        third_queue_turn(next_clock)
    elif (findmin(event_list) == 0): # from 0 to 0 | from 1 to 0
        area_under_b_t = round(area_under_b_t + (event_list[0] - clock), 3)
        # A
        T_i = round(event_list[0] + genExp(1), 3)
        # no need for C_i
        # B
        server_status = 1
        time_of_arrival.put(event_list[0])
        number_in_queue = time_of_arrival.qsize() - 1
        # C
        clock = event_list[0]
        event_list[0] = T_i
        # no need for event_list[1] = C_i
        # D
        # no need for number_serviced
        # no need for total_delay
        # no need for area_under_q_t
        next_clock = event_list[findmin(event_list)]
        second_queue_turn(next_clock)
        third_queue_turn(next_clock)
    elif (findmin(event_list) == 1):
        temp2 = time_of_arrival.get() # get out, your service is done.
        probability2 = round(genUniform(0, 1), 1)
        if (probability2 >= 0.4):
            if (time_of_arrival2.qsize() == 0):
                if (first_time_flag2 == True):
                    first_time2 = event_list[1]
                    first_time_flag2 = False
                T_i2 = event_list[1]
                D_i2 = 0
                C_i2 = round(T_i2 + D_i2 + genExp(4), 3)  # D_i = 0
                server_status2 = 1
                time_of_arrival2.put([T_i2, D_i2, C_i2])
                number_in_queue2 = time_of_arrival2.qsize() - 1
            else:
                T_i2 = event_list[1]
                D_i2 = round(time_of_arrival2.queue[0][2] - event_list[1], 3)
                C_i2 = round(T_i2 + D_i2 + genExp(4), 3)
                server_status2 = 1
                time_of_arrival2.put([T_i2, D_i2, C_i2])
                number_in_queue2 = time_of_arrival2.qsize() - 1
        probability3 = round(genUniform(0, 1), 1)
        if (probability3 <= 0.4):
            if (time_of_arrival3.qsize() == 0):
                if (first_time_flag3 == True):
                    first_time3 = event_list[1]
                    first_time_flag3 = False
                T_i3 = event_list[1]
                D_i3 = 0
                C_i3 = round(T_i3 + D_i3 + genExp(3), 3)  # D_i = 0
                server_status3 = 1
                time_of_arrival3.put([T_i3, D_i3, C_i3])
                number_in_queue3 = time_of_arrival3.qsize() - 1
            else:
                T_i3 = event_list[1]
                D_i3 = round(time_of_arrival3.queue[0][2] - event_list[1], 3)
                C_i3 = round(T_i3 + D_i2 + genExp(3), 3)
                server_status3 = 1
                time_of_arrival3.put([T_i3, D_i3, C_i3])
                number_in_queue3 = time_of_arrival3.qsize() - 1

        if (time_of_arrival.qsize() != 0):
            w_time_1 = round(w_time_1 + (event_list[1] - temp2), 3)
            area_under_b_t = round(area_under_b_t + (event_list[1] - clock), 3)
            D_i = round(event_list[1] - time_of_arrival.queue[0], 1)
            # A
            # no need for T_i
            C_i = round(time_of_arrival.queue[0] + D_i + genExp(2), 1)
            # B
            server_status = 1
            # no put
            number_in_queue = time_of_arrival.qsize() - 1
            # C
            clock = event_list[1]
            event_list[1] = C_i
            # no need for event_list[0] = T_i
            # D
            number_serviced = number_serviced + 1  # number_serviced + 1, because service for 1 customer is done.
            total_delay = round(total_delay + D_i, 3)
            # no need for area_under_q_t

        else:
            w_time_1 = round(w_time_1 + (event_list[1] - temp2), 3)
            area_under_b_t = round(area_under_b_t + (event_list[1] - clock), 3)
            # A
            # no need for T_i
            C_i = 99999
            # B
            server_status = 0
            # no put, get
            number_in_queue = time_of_arrival.qsize() # = 0
            # C
            clock = event_list[1]
            event_list[1] = C_i
            # no need for event_list[0] = T_i
            # D
            number_serviced = number_serviced + 1  # number_serviced + 1, because service for 1 customer is done.
            # no need for total_delay
            # no need for area_under_q_t

        next_clock = event_list[findmin(event_list)]
        second_queue_turn(next_clock)
        third_queue_turn(next_clock)
W_Q = 0
L_Q = 0
W = 0
E_S = 0
RO = 0
print(f'\ntotal number serviced is : {run}')
print('-----------------first queue-----------------')
percent = round((run - number_serviced2)/run * 100, 2)
print(f'number_serviced is: {run - number_serviced2}  {percent} %')
#print(time_of_arrival.queue)
if (time_of_arrival.qsize() == 0):
    print(f'total_delay is: {round(total_delay, 3)}')
else:
    print(f'total_delay is: {round(total_delay - D_i, 3)}')
if (time_of_arrival.qsize() == 0):
    W_Q = round(total_delay / number_serviced, 3)
    L_Q = round(total_delay / clock, 3)
    print(f'W_Q is : {W_Q}')
    print(f'L_Q is : {L_Q}')
else:
    W_Q = round((total_delay - D_i) / number_serviced, 3)
    L_Q = round((total_delay - D_i) / clock, 3)
    print(f'W_Q is : {W_Q}')
    print(f'L_Q is : {L_Q}')
if (time_of_arrival.qsize() == 0):
    E_S = round(S_i / number_serviced, 3)
    W = round(W_Q + E_S, 3)
    print(f'E_S is : {E_S}')
    print(f'W is : {W}')
else:
    E_S = round((S_i - temp_i)/ number_serviced , 3)
    W = round(W_Q + E_S, 3)
    print(f'E_S is : {E_S}')
    print(f'W is : {W}')
RO = round(area_under_b_t / clock, 3)
print(f'RO is : {RO}')
L = round(RO + L_Q, 3)
print(f'L is : {L}')
print(f'W_N is : {w_time_1}')
print('-----------------second queue-----------------')
percent = round(number_serviced2/run * 100, 2)
print(f'number_serviced is: {number_serviced2}  {percent} %')
#print(time_of_arrival2.queue)
print(f'total_delay is: {round(total_delay2, 3)}')
if (number_serviced2 != 0 and (clock - first_time2) != 0):
    W_Q = round(total_delay2 / number_serviced2, 3)
    print(f'W_Q is : {W_Q}')
    L_Q = round(total_delay2 / (clock - first_time2), 3)
    print(f'L_Q is : {L_Q}')
else:
    print(f'W_Q is : {0}')
    print(f'L_Q is : {0}')
if (number_serviced2 != 0 ):
    E_S = round(S_i2 / number_serviced2, 3)
    W = round(W_Q + E_S, 3)
    print(f'E_S is : {E_S}')
    print(f'W is : {W}')
else:
    print(f'E_S is : {0}')
    print(f'W is : {0}')
if (number_serviced2 and (clock - first_time2) != 0):
    RO = round(area_under_b_t2 / (clock - first_time2), 3)
    print(f'RO is : {RO}')
else:
    print(f'RO is : {0}')
if (number_serviced2 != 0 ):
    L = round(RO + L_Q, 3)
    print(f'L is : {L}')
else:
    print(f'L is : {0}')
print(f'W_N is : {w_time_2}')
print('-----------------Third queue-----------------')
percent = round(number_serviced3/run * 100, 2)
print(f'number_serviced is: {number_serviced3}  {percent} %')
#print(time_of_arrival3.queue)
print(f'total_delay is: {round(total_delay3, 3)}')
if (number_serviced3 != 0 and (clock - first_time3) != 0):
    W_Q = round(total_delay3 / number_serviced3, 3)
    print(f'W_Q is : {W_Q}')
    L_Q = round(total_delay3 / (clock - first_time3), 3)
    print(f'L_Q is : {L_Q}')
else:
    print(f'W_Q is : {0}')
    print(f'L_Q is : {0}')
if (number_serviced3 != 0 ):
    E_S = round(S_i3 / number_serviced3, 3)
    W = round(W_Q + E_S, 3)
    print(f'E_S is : {E_S}')
    print(f'W is : {W}')
else:
    print(f'E_S is : {0}')
    print(f'W is : {0}')
if (number_serviced3 and (clock - first_time3) != 0):
    RO = round(area_under_b_t2 / (clock - first_time3), 3)
    print(f'RO is : {RO}')
else:
    print(f'RO is : {0}')
if (number_serviced3 != 0 ):
    L = round(RO + L_Q, 3)
    print(f'L is : {L}')
else:
    print(f'L is : {0}')
print(f'W_N is : {w_time_3}')
print('---------------------------------------------')
print(f' Avg Response time : {round((w_time_1 + w_time_2 + w_time_3) / run, 3)}')
print('---------------------------------------------')
print(f' Avg Number of Customer : {round((number_serviced + number_serviced2 + number_serviced3) / run, 3)}')

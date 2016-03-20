from datetime import date
import calendar
# Hint:  use Google to find python function


####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

a_start = date_start.split("-")
a_start = map(int, a_start)
a_date1 = date(a_start[2], a_start[0], a_start[1])

a_stop = date_stop.split("-")
a_stop = map(int, a_stop)
a_date2 = date(a_stop[2], a_stop[0], a_stop[1])

a_ans = (a_date2 - a_date1).days
print "The answer to a) is %s days" % a_ans

####b)  
date_start = '12312013'  
date_stop = '05282015'  

n = 2
b_start = [date_start[i:i+n] for i in range(0,len(date_start),n)]
b_date1 = date( int(b_start[2] + b_start[3]), int(b_start[0]), int(b_start[1]))

b_stop = [date_stop[i:i+n] for i in range(0,len(date_stop),n)]
b_date2 = date( int(b_stop[2] + b_stop[3]), int(b_stop[0]), int(b_stop[1]))
b_ans = (b_date2 - b_date1).days
print "The answer to b) is %s days" %  b_ans

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

c_dict = {v: k for k, v in enumerate(calendar.month_abbr)}
c_list = [x for x in enumerate(calendar.month_abbr)]
c_start = date_start.split("-")
c_stop = date_stop.split("-")

c_start[1] = c_dict[c_start[1]] 
c_stop[1] = c_dict[c_stop[1]]

c_date1 = date(int(c_start[2]), c_start[1], int(c_start[0]))
c_date2 = date(int(c_stop[2]), c_stop[1], int(c_stop[0]))

c_ans = (c_date2 - c_date1).days
print "The answer to c) is %s days" % c_ans

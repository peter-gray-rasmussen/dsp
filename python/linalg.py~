import numpy as np
import sys

A = np.array([[1, 2, 3], [2, 7, 4]])

B = np.array([[1, -1], [0, 1]])

C = np.array([[5, -1], [9, 1], [6, 0]])
C_t = np.transpose(C)

D = np.array([[3, -2, -1], [1, 2, 3]])

u = np.array([ [6], [2], [-3], [5] ])

v = np.array([[3], [5], [-1], [4]])

w = np.array([ [1], [8], [0], [5] ])

# Question 1
print 40 * '*'
print 'Question 1'

# 1.1) 
print "1.1) The dimensions of A are %s" % str(A.shape)

# 1.2)
print '1.2) The dimensions of B are %s' % str(B.shape)

# 1.3)
print '1.3) The dimensions of C are %s' % str(C.shape)
print 'The dimensions of C_t are %s' % str(C_t.shape)

# 1.4)
print '1.4) The dimensions of D are %s' % str(D.shape)

# 1.5)
print '1.5) The dimensions of u are %s' % str(u.shape)

# 1.6)
print '1.6) The dimensions of w are %s' % str(w.shape)


# Question 2
print 40 * '*'
print 'Question 2'

alpha = 6

# 2.1)
print '2.1) u + v equals %s' % str(u + v)

# 2.2) 
print '2.2) u - v equals %s' % str(u - v)

# 2.3)
print '2.3) alpha * u equals %s' % str(alpha * u)

# 2.4)
print '2.4) u * v equals %s' % str(u * v)

u_sum = 0
u_sq = []
# 2.5) 
for i in u:
    u_sq.append(i**2)

for i in u_sq:
    u_sum += i

u_bar = u_sum**0.5

print '2.5) u_bar equals %s' % str(round(u_bar, 1))

# Question 3
print 40 * '*'
print 'Question 3'

# 3.1)
print '3.1) A + B is not defined'

# 3.2)
A - C_t
ans_3_2 = A - C_t
print '3.2) A - C_t equals %s' % ans_3_2

# 3.3) 
ans_3_3 = C_t + 3 * D
print '3.3) C_t + 3*D equals %s' % ans_3_3

# 3.4) 
print '3.4) BA is not defined'

# 3.5)
print '3.5) BA_t is not defined'

"""

You are a miner. You dig holes in the ground to collect gold. Thanks to your friend - the wizard you have magic glasses. Using them you can see which place in the ground is worth digging. What is more: you cannot dig everywhere. You cannot dig a hole in a place next to already existing hole. For example:

 

Having a ground G=[1,2,0,5,10]. When you dig on position 0 you will earn 1 gold sample (you know this, thanks to your magic glasses), but if you dig on position 0 you cannot dig on position 1, because position 1 is next to position 0. You might omit position 0 and start digging at position 1, but this way you will not be able to dig on position 2 and so on.

 

Your task is to provide a function that will tell you what is the maximum number of gold samples having in mind that we cannot dig in adjacent locations.

 

For example  having a ground:

G=[75, 105, 120, 75, 90, 135] 

The maximum number of gold samples is 330 (by digging 75+120+135)

"""


# 1: Skip the 2nd one
# 2: Skip the 1st one
# 3rd: Skip the 2nd & 3rd one 
# 4th: SKip the 1st and 2nd one
#[4] = 4
#==[4]
#[4,5] = 5
#==[4,5]
#[4,5,3] = 7 
#==[4,5,4+3]
#[4,5,3,6] = 4 * 3 + 2 * 1 # 4 comes in Save 4; 5 comes in save 5; 3 comes in save; 6 comes in save; 
#==[4,5,4+3,5+6] 
# 4 * (n/3) ; O(n)
ground = [4,5,3,6]
ground = [75, 105, 120, 75, 90, 135] 

max_sequence = []
for i, g in enumerate(ground, start=0):
    max_value = g
    ### Comparisons
    if len(max_sequence) > 1:
        # Options:
        # Skip current; Skip previous; Skip previous two
        options = [max_sequence[i-2] + g, max_sequence[i-1]]
        if len(max_sequence) > 2:
            options.append(max_sequence[i-3] + g)
        max_value = max(options)
    ### Add current max
    max_sequence.append(max_value)
print(max_sequence)
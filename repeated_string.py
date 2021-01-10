s, n = input().strip() ,int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))



# logic 

# 1 ->  first count the a in arr or string
# 2 ->  divide the times with len(arr) (get in int) 
# 3 ->  Now multiply with counted a 
# 4 -> if the times odd the find the mod with len and add this in your counted 'a'
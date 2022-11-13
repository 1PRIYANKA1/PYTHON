#Accept initial velocity (u), acceleration (a) and time (t). Print the final velocity (v) and the distance (s) travelled. (Hint: v = u + at, s = u + at2) 
v=float(input("enter the velocity"));
print(v)
a=float(input("enter the acceleration"));
print(a);
t=int(input("enter the time"));
print(t);
fv=v+a*t
print(fv);
distance=v+at*t
print(distance);

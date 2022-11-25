import turtle
#context-free grammar L-system
def iterate(axiom): #only 1 char left side
    nstr=''
    for i in range(0, len(axiom)):
        b=False
        for k in rules.keys():
            if axiom[i]==k:
                nstr+=rules[k]
                b=True
        if b==False:
            nstr+=axiom[i]
    return nstr

def move(str, angle, length, k):
    #begin_fill()
    turtle.speed('fastest')
    turtle.hideturtle()
    turtle.goto(-350, 0)
    x=[]
    y=[]
    a=[]
    lenarr=[]
    #length=30
    for i in range(0, len(str)):
        if str[i]=='F':
            turtle.forward(length)
        if str[i]=='f':
            turtle.up()
            turtle.forward(length)
            turtle.down()
        if str[i]=='+':
            turtle.left(angle)
        if str[i]=='-':
            turtle.right(angle)
        if str[i]=='[':
            x.append(turtle.xcor())
            y.append(turtle.ycor())
            a.append(turtle.heading())
            lenarr.append(length)
        if str[i]==']':
            turtle.up()
            turtle.goto(x.pop(),y.pop())
            ang=float(a.pop())
            length=float(lenarr.pop())
            turtle.setheading(ang)
            turtle.down()
        if str[i]=='>':
            length*=k
        if str[i]=='<':
            length/=k

print('Enter axiom:')
axiom=str(input())
print('Enter rules. Use -> for arrows and do not use spaces. Enter \'done\' when done.')
rules={}
while True:
    s=str(input())
    if(s=='done'):
        break
    st=s.split('->')
    a=st[0]
    b=st[1]
    rules[a]=b
print('Enter angle (degrees)')
angle=float(input())
print('Enter iterations')
n=int(input())
print('Enter starting line length')
l=float(input())
print('Enter line length factor')
k=float(input())
for i in range(0, n):
    axiom=iterate(axiom)
move(axiom, angle, l, k)


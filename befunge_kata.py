import random

def interpret(code):
    output = [""]
    stack = []
    position = [0,0]
    direction = [">"]
    codefield = [list(x) for x in code.split("\n")]
    run = [True]
    
    def step(n):
        if n == "<":
            position[0] -= 1
            if position[0] < 0:
                position[0] = len(codefield[position[1]])-1
        elif n == ">":
            position[0] += 1
            if position[0] > len(codefield[position[1]])-1:
                position[0] = 0
        elif n == "v":
            position[1] += 1
            if position[1] > len(codefield):
                position[1] = 0
        elif n == "^":
            position[1] -= 1
        if position[1] < 0:
            position[1] = len(codefield)-1

    def push(n):
        stack.append(n)

    def add(n):
        a= stack.pop()
        b= stack.pop()
        stack.append(int(a)+int(b))

    def sub(n):
        a= stack.pop()
        b= stack.pop()
        stack.append(int(b)-int(a))

    def mult(n):
        a= stack.pop()
        b= stack.pop()
        stack.append(int(a)*int(b))

    def divin(n):
        a= stack.pop()
        b= stack.pop()
        if int(a) == 0:
            stack.append(0)
        else:
            stack.append(int(b)/int(a))

    def modu(n):
        a= stack.pop()
        b= stack.pop()
        if int(a) == 0:
            stack.append(0)
        else:
            stack.append(int(b)%int(a))

    def logical_not(n):
        a= stack.pop()
        if a == 0:
            stack.append(1)
        else:
            stack.append(0)

    def greater(n):
        a= stack.pop()
        b= stack.pop()
        if b>a:
            stack.append(1)
        else:
            stack.append(0)

    def right(n):
        direction[0] = n

    def left(n):
        direction[0] = n

    def up(n):
        direction[0] = n

    def down(n):
        direction[0] = n

    def random_direktion(n):
        direction[0] = random.choice(["<",">","v","^"])

    def pop_hor(n):
        if int(stack.pop()) != 0:
            direction[0] = "<"
        else:
            direction[0] = ">"

    def pop_vert(n):
        if int(stack.pop()) != 0:
            direction[0] = "^"
        else:
            direction[0] = "v"

    def stringmode(n):
        str_mode = True
        while str_mode:
            step(direction[0])
            if codefield[position[1]][position[0]] == '"':
                str_mode = False
            else:
                push(ord(codefield[position[1]][position[0]]))

    def duplicate(n):
        if len(stack) > 0:
            stack.append(stack[-1])
        else:
            stack.append(0)

    def swap(n):
        if len(stack) == 0:
            pass
        elif len(stack) == 1:
            stack.insert(0,0)
        elif len(stack) > 1:
            stack[-2],stack[-1] = stack[-1],stack[-2]

    def discard(n):
        stack.pop()

    def intpop(n):
        output.append(stack.pop())

    def ascipop(n):
        output.append(chr(stack.pop()))

    def trampoline(n):
        step(direction[0])

    def put(n):
        y = stack.pop()
        x = stack.pop()
        v = stack.pop()
        codefield[int(y)][int(x)] = chr(int(v))

    def get(n):
        y = stack.pop()
        x = stack.pop()
        stack.append(ord(codefield[int(y)][int(x)]))

    def iddle(n):
        pass

    def end_prog(n):
        run[0] = False

    befunge = {
        "push" : push,
        "+" : add, 
        "-" : sub,
        "*" : mult,
        "/" : divin,
        "%" : modu,
        "!" : logical_not,
        "`" : greater,
        "<" : left,
        ">" : right,
        "v" : down,
        "^" : up,
        "?" : random_direktion,
        "_" : pop_hor,
        "|" : pop_vert,
        '"' : stringmode,
        ":" : duplicate,
        "\\" : swap,
        "$" : discard,
        "." : intpop,
        "," : ascipop,
        "#" : trampoline,
        "p" : put,
        "g" : get,
        " " : iddle,
        "@" : end_prog
    }

    while True:
        
        if not run[0]:
            break
        command = codefield[position[1]][position[0]]
        
        if command.isdigit():
            befunge["push"](command)
        else:
            
            befunge[command](command)
            
        step(direction[0])
    
    for i in range(len(output)):
        output[i] = str(output[i])
    return "".join(output)
    


print(interpret('>987v>.v\nv456<  :\n>321 ^ _@'), '123456789')
print(interpret('08>:1-:v v *_$.@\n  ^    _$>\:^'),"40320")


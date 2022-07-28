zero = '+[]'
one = '+!![]'

number = lambda n: " + ".join((one for i in range(n))) if n else zero

def fromString(s):
    return "+".join((map[x] for x in s))

map = {}

map["a"] = f"(+{{}}+[])[{number(1)}]"
map["b"] = f"({{}}+[])[{number(2)}]"
map["o"] = f"({{}}+[])[{number(1)}]"
map["e"] = f"({{}}+[])[{number(4)}]"
map["c"] = f"({{}}+[])[{number(5)}]"
map["t"] = f"({{}}+[])[{number(6)}]"
map[" "] = f"({{}}+[])[{number(7)}]"
map["f"] = f"(![]+[])[{number(0)}]"
map["s"] = f"(![]+[])[{number(3)}]"
map["r"] = f"(!![]+[])[{number(1)}]"
map["u"] = f"(!![]+[])[{number(2)}]"
map["i"] = f"((+!![]/+[])+[])[{number(3)}]"
map["n"] = f"((+!![]/+[])+[])[{number(4)}]"
map["S"] = f"([]+([]+[])[{fromString('constructor')}])[{number(9)}]"
map["g"] = f"([]+([]+[])[{fromString('constructor')}])[{number(14)}]"
map["p"] = f"([]+(/-/)[{fromString('constructor')}])[{number(14)}]"
map['\\'] = f"(/\\\\/+[])[{number(1)}]"
import math
import os
import sys
import time
import random
import string

random.seed(time.time())
charlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_"
charlist_length = len(charlist)
header_charlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
header_charlist_length = len(header_charlist)


def getChar(chars, charscount, i):
    idx = i % charscount + 1
    return chars[idx]


def getRandomChar():
    return getChar(charlist, charlist_length, random.randint(1, charlist_length))


def getRandomHChar():
    return getChar(header_charlist, header_charlist_length, random.randint(1, charlist_length))


def getRandomName(l):
    r = getRandomHChar()
    for _ in range(2, l):
        r = r + getRandomChar()
    return r


base_type_and_default = {
    "bool": "false",
    "int": "0",
    "float": "0.0f",
    "double": "0.0",
    "string": "null"
}


def bool_function(a, b, c):
    r = random.randint(1, 5)
    if r == 1:
        return [a + " = " + b + " && " + c + ";", ]
    elif r == 2:
        return [
            "if(" + a + ") ",
            "{",
            "    " + b + " = !" + c + ";",
            "}",
        ]
    elif r == 3:
        return [
            "if(" + a + " && " + c + ") ",
            "{",
            "    " + b + " = !" + b + ";",
            "}",
        ]
    elif r == 4:
        return [
            "if(" + a + " || " + b + ") ",
            "{",
            "    " + b + " = !" + b + ";",
            "}",
        ]
    elif r == 5:
        return [a + " = " + b + " || " + c + ";", ]
    else:
        return [a + " = " + b + " && " + c + ";", ]


def int_function(a, b, c):
    r = random.randint(1, 7)
    if r == 1:
        return [a + " = " + b + " + " + c + ";", ]
    elif r == 2:
        return [a + " = " + b + " - " + c + ";", ]
    elif r == 3:
        return [a + " = " + b + " * " + c + ";", ]
    elif r == 4:
        return [a + " = " + b + " / " + c + ";", ]
    elif r == 5:
        return [
            a + " = " + str(random.randint(1, 100000)) + ";",
            b + " = " + str(random.randint(1, 100000)) + ";",
            c + " = " + str(random.randint(1, 100000)) + ";",
        ]
    elif r == 6:
        return [
            "for(int i=0;i<" + a + ";++i)",
            "{",
            "	" + b + "+=1;",
            "   " + c + "+=" + b + ";",
            "}",
        ]
    else:
        return [
            b + " = " + a + ";",
            c + " = " + a + ";",
        ]


def float_function(a, b, c):
    r = random.randint(1, 6)
    if r == 1:
        return [a + " = " + b + " + " + c + ";", ]
    elif r == 2:
        return [a + " = " + b + " - " + c + ";", ]
    elif r == 3:
        return [a + " = " + b + " * " + c + ";", ]
    elif r == 4:
        return [a + " = " + b + " / " + c + ";", ]
    elif r == 5:
        return [
            a + " = " + str(random.randint(1, 100000)) + ".0f;",
            b + " = " + str(random.randint(1, 100000)) + ".0f;",
            c + " = " + str(random.randint(1, 100000)) + ".0f;",
        ]
    else:
        return [
            b + " = " + a + ";",
            c + " = " + a + ";",
        ]


def double_function(a, b, c):
    r = random.randint(1, 6)
    if r == 1:
        return [a + " = " + b + " + " + c + ";", ]
    elif r == 2:
        return [a + " = " + b + " - " + c + ";", ]
    elif r == 3:
        return [a + " = " + b + " * " + c + ";", ]
    elif r == 4:
        return [a + " = " + b + " / " + c + ";", ]
    elif r == 5:
        return [
            a + " = " + str(random.randint(1, 100000)) + ".0;",
            b + " = " + str(random.randint(1, 100000)) + ".0;",
            c + " = " + str(random.randint(1, 100000)) + ".0;",
        ]
    else:
        return [
            b + " = " + a + ";",
            c + " = " + a + ";",
        ]


def string_function(a, b, c):
    r = random.randint(1, 3)
    if r == 1:
        return [a + " = " + b + " + " + c + ";", ]
    elif r == 2:
        return [
            a + " = string.Format(" + c + "," + b + ");",
        ]
    else:
        return [
            b + " = " + a + ";",
            c + " = " + a + ";",
        ]


# base_type_randomfunction = {}

base_type_list = None
property_info = {
    "p": "",
    "name": "default",
    "t": "int",
    "v": "0",

}
attribute_info = {
    "p": "",
    "name": "default",
    "t": "int",
    "property_info": None,
}


def getRandomType():
    base_type_list = None
    if base_type_list == None:
        base_type_list = []
        for k, _ in base_type_and_default.items():
            base_type_list.append(k)
    r = random.randint(1, len(base_type_list))
    t = base_type_list[r]
    return t, base_type_and_default[t]


def getRandomPublic():
    r = random.randint(1, 3)
    if r == 1:
        return "public"
    elif r == 2:
        return "private"
    else:
        return ""


def PropertyGenerate(p, n, t, v):
    ta = property_info
    ta["p"] = p
    ta["name"] = n
    ta["t"] = t
    ta["v"] = v
    return ta


def AttributeGenerate(p, n, t, pi):
    ta = attribute_info
    ta["p"] = p
    ta["name"] = n
    ta["property_info"] = pi
    if pi != None:
        ta["t"] = pi["t"]
    return ta


method_info = {
    "p": "",
    "name": "default",
    "params": None,
    "retn": None,
    # "content": None,
}


def MethodContentGenerate(ci) -> list:
    base_type_randomfunction = [
        int_function,
        float_function,
        double_function,
        string_function,

    ]
    content = []
    for i in range(1, 10):
        t, v = getRandomType()
        m = ci["typemap"][t]

        f = base_type_randomfunction[int(t)]
        if len(m) > 0:
            a = random.choice(m)
            c = f(a, random.choice(m), random.choice(m))
            for v in c:
                content.append(v)
    return content


def MethodGenerate(ci, p, n, r):
    ta = method_info
    ta["p"] = p
    ta["name"] = n
    ta["retn"] = r
    ta["content"] = MethodContentGenerate(ci)
    return ta


class_info = {
    "p": "",
    "name": "default",
    "implement": None,
    "properties": None,
    "attributes": None,
    "typemap": None,
}
classes = []
classnames = {}


def GetNextClassName(min, max):
    r = random.randint(min or 10, max or 10)
    while True:
        n = getRandomName(r)
        if classnames[n] == None:
            classnames[n] = True
            return n


def GetNextName(min, max):
    usedname = {}
    r = random.randint(min or 10, max or 10)
    while True:
        n = getRandomName(r)
        if usedname[n] == None:
            usedname[n] = True
            return n


def ClassGenerater(mc, pc, ac):
    class_info = {"p": "", "name": GetNextClassName(10, 40), "implement": "MonoBehaviour", "properties": [],
                  "attributes": None, "typemap": None}

    for i in range(1, pc or 20):
        class_info["properties"].append(
            PropertyGenerate(
                getRandomPublic(),
                GetNextName(10, 40),
                getRandomType()
            ))
    class_info["attributes"] = []
    for i in range(1, ac or 20):
        t, v = getRandomType()
        pi = None
        if random.randint(1, 10) < 3:
            pi = class_info["properties"][random.randint(1, len(class_info["properties"]))]
        class_info["attributes"].append(
            AttributeGenerate(
                "public",
                GetNextName(10, 40),
                t, pi
            ))
    class_info["typemap"] = {}
    for _, v in enumerate(base_type_list):
        class_info["typemap"][v] = []
    for _, v in enumerate(class_info["properties"]):
        class_info["typemap"][v["t"]].append(v["name"])
    for _, v in enumerate(class_info["attributes"]):
        class_info["typemap"][v["t"]].append(v["name"])
    class_info["methods"] = []
    for i in range(1, mc or 20):
        t, v = getRandomType()
        pi = None
        if random.randint(1, 10) < 3:
            pi = class_info["properties"][random.randint(1, len(class_info["properties"]))]
        class_info["methods"].append(
            MethodGenerate(class_info, "public", GetNextName(10, 40), t))
    return class_info


typemap = {}
base_type_list = []
for _, v in enumerate(base_type_list):
    typemap[v] = []
for i in range(1, 100):
    classes.append(ClassGenerater(10, 10, 10))
    # print(classes[i-1])
    for _, v in enumerate(classes[i - 1]["properties"]):
        typemap[v["t"]].append(v["name"])
    for _, v in enumerate(classes[i - 1]["attributes"]):
        typemap[v["t"]].append(v["name"])
    for _, v in enumerate(classes[i - 1]["methods"]):
        typemap[v["retn"]].append(v["name"])
    for _, v in enumerate(classes[i - 1]["methods"]):

        for _, v2 in enumerate(v["content"]):
            typemap[v2["t"]].append(v2["name"])
    # print(classes[i-1])
    # print(typemap)
    # print(classes[i-1]["methods"][0]["content"])
    # print(classes[i-1]["methods"][0]["content"][0]["name"])
    # print(classes[i-1]["methods"][0]["content"][0]["t"])

methods = {}
for i in range(1, 20):
    t, v = getRandomType()
    if random.randint(1, 10) < 3:
        pi = classes[0]["properties"][random.randint(1, len(classes[0]["properties"]))]
    methods[i] = MethodGenerate(classes[0], "public", GetNextName(10, 40), t)
    # print(methods[i])
    # print(methods[i]["content"])


def GetClassSource(class_info):
    r = ""
    t = 0

    def s(str):
        nonlocal r
        nonlocal t
        for i in range(1, t):
            r = r + "    "
        r = r + str + "\r\n"

    def _property(p):
        s(p["p"] + " " + p["t"] + " " + p["name"] + " = " + p["v"] + ";")

    def _attribute(a):
        t = 0
        s(a["p"] + " " + a["t"] + " " + a["name"])
        t = t + 1

        if a["property_info"]:
            p = a["property_info"]
            s("get { return " + p["name"] + "; }")
            s("set { " + p["name"] + " = value; }")
        else:
            s("get;")
            s("set;")
        t = t - 1

    if class_info["properties"] != None:
        for _, p in enumerate(class_info["properties"]):
            _property(p)
    if class_info["attributes"] != None:
        for _, p in enumerate(class_info["attributes"]):
            _attribute(p)
    if class_info["methods"] != None:
        for _, m in enumerate(class_info["methods"]):
            ty = "void"
            if m["retn"] != None:
                ty = m["retn"][1]
            p = "()"
            if m["params"] != None:
                p = ""
                for _, v in enumerate(m["params"]):
                    if len(p) > 0:
                        p = p + "," + v[1] + " " + v[2]
                    else:
                        p = v[1] + " " + v[2]
                p = "(" + p + ")"
            s(m["p"] + " " + ty + " " + m["name"] + p)
            t = t + 1

            for _, v in enumerate(m["content"]):
                s(v)
            t = t - 1
    return r


def s(str):
    r = ""
    t = 0
    for i in range(1, t):
        r = r + "    "
    r = r + str + "\r\n"
    return r


def _property(p):
    s(p["p"] + " " + p["t"] + " " + p["name"] + " = " + p["v"] + ";")


def _attribute(a):
    t = 0
    s(a["p"] + " " + a["t"] + " " + a["name"])
    t = t + 1

    if a["property_info"]:
        p = a["property_info"]
        s("get { return " + p["name"] + "; }")
        s("set { " + p["name"] + " = value; }")
    else:
        s("get;")
        s("set;")
    t = t - 1


def precent_bar(v, l):
    p = [".", "-", "="]
    pl = len(p)
    line = ""
    per = v
    s = per * l
    n = math.floor(s)
    ns = math.floor((s - n) * pl) + 1
    for i in range(1, l):
        if i < n + 1:
            line = line + p[pl]
        elif i == n + 1:
            line = line + p[ns]
        else:
            line = line + p[1]
    return line


help_messagr = """
C# Garbage Code Generater
    -h: Help
    -o: Output Dir, Default="garbate"
    -c: Generate Class Count, Default=400
    -mc: Method Count, Default=30
    -pc: Property Count, Default=30
    -ac: Attribute Count, Default=30
    -verbose: Print Every Generate Class Name
    -q: QuietMode, Print Nothing
"""


def main():
    name = "garbage"
    class_count = 400
    method_count = 30
    property_count = 30
    attribute_count = 30
    verbose = False
    quiet = False

    if sys.argv:
        len = len(sys.argv)
        for i in range(1, len):
            v = sys.argv[i]
            if v == "--h" or v == "--H" or v == "-h" or v == "-H" or v == "?":
                print(help)
                return
            elif (v == "-c" or v == "--c") and i < len:
                i = i + 1
                class_count = 0
            elif (v == "-o" or v == "--o") and i < len:
                i = i + 1
                name = sys.argv[i]
            elif (v == "-mc" or v == "--mc") and i < len:
                i = i + 1
                method_count = 0
            elif (v == "-pc" or v == "--pc") and i < len:
                i = i + 1
                property_count = 0
            elif (v == "-ac" or v == "--ac") and i < len:
                i = i + 1
                attribute_count = 0
            elif v == "-verbose":
                verbose = True
            elif v == "-q" or v == "-quiet":
                quiet = True

    if not quiet:
        print("Generating...")
    if not os.path.exists(name):
        os.mkdir(name)
    for i in range(1, class_count):
        class_info = ClassGenerater(method_count, property_count, attribute_count)
        class_code = GetClassSource(class_info)
        file = open(name + "/" + class_info["name"] + ".cs", "w")
        file.write(class_code)
        file.close()
        if verbose:
            print("Generated: " + class_info["name"])
    if not quiet:
        print("Done!")
    if not quiet:
        print("output = " + name)
        print("class count = " + str(class_count))
        print("method count = " + str(method_count))
        print("property count = " + str(property_count))
        print("attribute count = " + str(attribute_count))
    path = name + "/"
    try:
        os.mkdir(name)
    except:
        pass
    for i in range(1, class_count):
        class_info = ClassGenerater(method_count, property_count, attribute_count)
        file = open(path + class_info["name"] + ".cs", "w")
        file.write(GetClassSource(class_info))
        file.close()
        if not quiet:
            if verbose:
                print(class_info["name"] + ".cs")
            else:
                print("\013" + "|" + precent_bar(i / class_count, 60) + "| " + string.format("%5d/%5d", i, class_count))
    if not quiet:
        print("\nFin!")


main()

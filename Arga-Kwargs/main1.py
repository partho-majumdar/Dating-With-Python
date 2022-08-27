def fun_args(normal, *args, **kwargs):
    print(normal)

    for itme in args:
        print(itme)

    for key, value in kwargs.items():
        print(f"Key is {key} and value is {value}")


var1 = "This is normal parameter"
var2 = [1, 2, 3, 4, 5, 6]
var3 = {
    "A": "aa",
    "B": "bb",
    "C": "cc",
    "D": "dd",
}

fun_args(var1, *var2, **var3)

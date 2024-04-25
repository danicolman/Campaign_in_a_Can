import functions as f
import config
import inspect

coda_webhooks = [i for i in config.config.keys() if "RULE" in i]
all_funcs = inspect.getmembers(f, inspect.isfunction)
funcs = [i[0] for i in all_funcs]
print(inspect.getmembers(f, inspect.isfunction))

func_dict = {}

# Dynamically match existing webhooks to functions
for i in coda_webhooks:
    thing = i.replace("_RULE", "").lower()
    for c in funcs:
        x = funcs.index(c)
        if thing in c:
            c_func = all_funcs[x]
            func_dict.update({thing: {"webhook": i, "function": c_func[1]}})

print(func_dict)

for key in func_dict.keys():
    f.send_to_coda(function[key]["webhook"], f.dnd_itereable(function[key]["function"]))

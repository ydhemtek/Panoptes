import os

def print_motd() :
    print("\033[34m" + r"""
                                       __                 
    ___________    ____   ____ _______/  |_  ____   ______
    \____ \__  \  /    \ /  _ \\____ \   __\/ __ \ /  ___/
    |  |_> > __ \|   |  (  <_> )  |_> >  | \  ___/ \___ \ 
    |   __(____  /___|  /\____/|   __/|__|  \___  >____  >
    |__|       \/     \/       |__|             \/     \/ 
    """ + "\033[0m")

if globals().get('menu') is None:
    menu = []

class modules :
    def __init__(self,f,desc = "My Panoptes module") :
        self.desc = desc
        self.f = f

    def new(*args, **kwargs) :
        def inner(f) :
            r = modules(f,args[0])
            menu.append(r)
        return inner

def parse_prior(mname) :
    with open(mname,'r') as f :
        lines = f.readlines()
        for line in lines :
            if line.startswith("#priority") :
                return int(line.split(":")[1].strip())
    return 9999999999
def list_modules():
    modules = []
    for module in os.listdir("modules"):
        if module.endswith(".py"):
            ctime = os.path.getctime(os.path.join("modules", module))
            priority = parse_prior(os.path.join("modules", module))
            modules.append((ctime, priority, module))
    modules.sort(key=lambda x: (x[1], x[0]))
    return [x[2] for x in modules]

def main():
    retry = None
    while retry != False:
        for i in menu :
            print(f"[{menu.index(i)+1}] - {i.desc}")
        number = str(input("\nChoose a number : "))
        if not number in [str(x+1) for x in range(0, len(menu))]:
            print(f"Wrong number, try again.")
        else:
            number = int(number)-1
            menu[number].f()
            retry = False

if __name__ == "__main__" :
    print_motd()
    for module in list_modules():
        module = module[:-3]
        m = __import__(f"modules.{module}", fromlist=[module])
        menu = m.menu
    main()

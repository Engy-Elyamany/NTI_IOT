import my_module.url_module as url

c = 'y'
while c == 'y':
    print("MENU : ")
    for num,(name,_) in url.sites.items():
        print(f"{num} => {name}")

    get_choice = int(input("Enter your choice : "))
    if get_choice in url.sites.keys() :
        url.open_url(url.sites[get_choice][1])
    else:
        print("invalid input, Not found in menu \n Input the desired website's URL")
        u = input()
        url.open_url(u)  
    c = input("Try another website [y/n] : ")


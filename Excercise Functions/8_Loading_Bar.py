def loadingBar(perc):
    loaded = int(perc / 10)
    missing = 10 - loaded
    load_bar = f"[{loaded * '%'}{missing * '.'}]"
    if loaded == 10:
        print("100% Complete!")
        print(load_bar)
    else:
        print(f"{perc}% {load_bar}")
        print('Still loading...')


percentage = int(input())
loadingBar(percentage)

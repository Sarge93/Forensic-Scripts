import winreg

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')


def convertation(value):
    res = []
    for i in range(0,len(value),2):
        res.append(value[i+1] * 256 + value[i])
    return res

def beautiful_print(value):
    print("{}, {} {} {} {}:{}:{}.{}".format(days[value[2]], value[3], months[value[1] - 1], value[0], value[4], value[5], value[6], value[7]))

if __name__ == "__main__":
    with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey_lm:
        with winreg.OpenKey(hkey_lm, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles\{B9D26F3A-B591-4F81-BFBD-6CDA6322D8AB}", 0, winreg.KEY_ALL_ACCESS) as current_key:
            dateCreated = winreg.QueryValueEx(current_key, "DateCreated")[0]
            dateLastConnected = winreg.QueryValueEx(current_key, "DateLastConnected")[0]
            print("DateCreated: ", end="")
            beautiful_print(convertation(dateCreated))
            print("DateLastConnected: ", end="")
            beautiful_print(convertation(dateLastConnected))
            print()
        with winreg.OpenKey(hkey_lm, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles\{E26FD9AC-AD4E-4171-B4CD-4C34F91C5E00}", 0, winreg.KEY_ALL_ACCESS) as current_key:
            dateCreated = winreg.QueryValueEx(current_key, "DateCreated")[0]
            dateLastConnected = winreg.QueryValueEx(current_key, "DateLastConnected")[0]
            print("DateCreated: ", end="")
            beautiful_print(convertation(dateCreated))
            print("DateLastConnected: ", end="")
            beautiful_print(convertation(dateLastConnected))
        

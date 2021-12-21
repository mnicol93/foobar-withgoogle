def solution(msg):
    letterVal = 0
    str = list(msg)
    
    for i in range(len(msg)):
        letterVal = ord(msg[i]) - 97
        if letterVal >= 0 and letterVal < 26:
            str[i] = chr((25-letterVal)+97)                
        
    return ("".join(str))

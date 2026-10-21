def main():
    GB = input("Enter GB used: ")
    baseCost = float(input("Enter base cost: "))
    over = AmIOver(GB)
    bill = baseCost
    if (over):
        overAmnt = GB-10
        extraCharge = overAmnt*2
        bill = baseCost + extraCharge
        if (overAmnt>5):
            usage = 'high'
        else:
            usage = 'moderate'
    else:

        print('Your bill is ${bill}')
        

def AmIOver(GB):
    if (GB>10):
        return True
    else:
        return False
    

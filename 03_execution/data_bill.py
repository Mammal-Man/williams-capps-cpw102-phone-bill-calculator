def main():
    GB = float(input("Enter GB used: "))
    baseCost = round(float(input("Enter base cost: ")), 2)
    over = AmIOver(GB)
    bill = baseCost
    if (over):
        overAmnt = GB-10
        print(f"you are {overAmnt} GB over your limit")
        extraCharge = round(overAmnt*2, 2)
        bill += extraCharge
        if (overAmnt>5):
            usage = 'high'
        else:
            usage = 'moderate'
        print(f"{usage} extra usage.")
    else:
        print("You are within your limit")
    print(f"your bill is ${bill}")    

def AmIOver(GB):
    if (GB > 10):
        return True
    else:
        return False

main()
    

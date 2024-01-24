def compute_postage(amount, stamps):
    if amount == 28:
        stamps[5]+=4
        stamps[8]+=1
    elif amount == 29:
        stamps[5]+=1
        stamps[8]+=3
    elif amount == 30:
        stamps[5]+=6
    elif amount == 31:
        stamps[5]+=3
        stamps[8]+=2
    elif amount > 31:
        stamps[5]+=1
        compute_postage(amount-5, stamps)

    return stamps

def main():
    for i in range(28, 101):
        stamps = {
            5: 0,
            8: 0
        }
        compute_postage(i, stamps)
        print(f"Postage for {i} is: {stamps}")

if __name__ =='__main__':
    main()
bal= 500
def withdraw(bal, request):

    result = bal

    if request > bal:
        print("No sufficient funds available ")

    elif request < 0:
        print("Please enter more than zero! ")

    else:
        result = bal - request

        while request > 0:

            if request >= 100:
                request -=100
                print("give 100")

            elif request >= 50:
                request -= 50
                print("give 50")

            elif request >= 10:
                request -= 10
                print("give 10")

            elif request >= 5:
                request -= 5
                print("give 5")

            elif request < 5:
                print("give "+ str(request))
                request = 0



    return result



bal = withdraw(bal, 278)
bal = withdraw(bal, 32)
bal = withdraw(bal, 37)

print(bal)
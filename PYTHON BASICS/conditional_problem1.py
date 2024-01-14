# take user input
tunnel_length=int(input("enter the length of the tunnel:"))
if tunnel_length<100:
    print("the tunnel is a short tunnel")
elif tunnel_length>100 and tunnel_length<500:
    print("the tunnel is a medium tunnel")
else:
    print("the tunnel is a long tunnel")
    
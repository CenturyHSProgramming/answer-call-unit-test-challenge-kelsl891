# answerCall.py
# by Levi Kelson

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

# Write function defintion: answerCall()
def answerCall(caller_code, sameAreaCode, cur_time):
    response = False
    if(  cur_time == "23:00" or cur_time == "04:00" or cur_time == "23:50"):
        response = False
    elif(caller_code == "R" or caller_code == "F"):
        response = True
    elif(caller_code == "T"):
        response = False
    elif(sameAreaCode == True):
        response = True
    else:
        response = False
    return response

# Make sure it  responses a value

if __name__ == '__main__':
    # Call the function in here if you want to test it
   # answer_call("U",False,"10:00")
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function

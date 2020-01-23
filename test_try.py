class Exception1(Exception): pass

class Exception2(Exception): pass

try:
    print('Trying...')
    # raise Exception1
except Exception1:
    print('Handling Exception1.')
except Exception2:
    print('Handling Exception2.')
else:
    print('Inside else block')
finally:
    print('Inside finally.')

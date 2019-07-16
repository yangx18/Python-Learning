from goto import with_goto

@with_goto
def range(start, stop):
    a = 0
    i = start
    result = []

    label .begin
    a = a +1
    
    if i == stop:
        print(a)
        goto .end

    result.append(i)
    i += 1
    goto .begin

    label .end
    print('now it is over')
    return result

start = input('input where u want to start')
stop = input('input where u want to stop')

range(start,stop)
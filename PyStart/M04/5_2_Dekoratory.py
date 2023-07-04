from time import sleep, time
def get_execution_details(function):
    def wrapper(*args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)
        start = time()
        output = function(*args, **kwargs)
        end = time()
        print(f"Execution timr {end-start}.")
        return output
    return wrapper

@get_execution_details
def go_to_sleep(time):
    sleep(time)
    print("spac")
    sleep(time)

go_to_sleep(3)

# czesciej sie korzysta z gotowych dekoratorow
# przesledz debugerem bo inaczej nie da sie po kolei przesledzic
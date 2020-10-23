import time
import threading

test_arr = [5, 1, 9, 2, 8, 6, 10, 4]

#AN "STANDARD" IMPLEMENTATION OF MERGESORT FOR ARRAYS (LISTS)
def mergesort(arr):

    len_arr = len(arr)

    if(len_arr <= 1):
        return arr

    middle = (len_arr // 2) #MUST BE INTEGER

    #print(middle)

    left = mergesort(arr[middle:])
    right = mergesort(arr[:middle])

    return merge(left, right)

def merge(left, right):

    left_walker, right_walker = 0, 0
    merged = []

    while((left_walker < len(left)) and right_walker < len(right)):
        if(left[left_walker] < right[right_walker]):
            merged.append(left[left_walker])
            left_walker+=1
        else:
            merged.append(right[right_walker])
            right_walker+=1

    #IF SOMETHING REMAINS, ADD TO THE END
    if left_walker < len(left):
        merged.extend(left[left_walker:])
    else:
        merged.extend(right[right_walker:])

    return merged

#print(test_arr)

#res = mergesort(test_arr)

#print(res)

#WRAPPER FOR CALLING THREAD ON MERGESORT
def worker_mergesort(thread_number, arr, result):
    
    print("Thread " + str(thread_number) + " started")

    thread_res = mergesort(arr)

    print("Thread " + str(thread_number) + " ended")

    result.append(thread_res)

def exec():
    
    arr = [5, 1, 9, 2, 8, 6, 10, 4, 7, 3]

    threads = []
    qnt_threads = 2

    result = [] #UGLY AND DANGEROUS, BUT WORKS...

    #PARTITIONING THE ARRAY CAUSES MORE OVERHEAD... ¯\_(ツ)_/¯

    #TODO: HANDLE MORE THAN 2 PARTITIONS (IS IT POSSIBLE/DOABLE?)

    #partitions = []

    middle = len(arr) // qnt_threads #WILL CHANGE COMPLETELY IF THERE ARE MORE PARTITIONS

    for i in range(qnt_threads):

        t = threading.Thread(target=worker_mergesort, args=( (i + 1), arr[ i * middle : (i + 1) * middle ], result ))
        #print(arr[ i * middle : (i + 1) * middle ])
        threads.append(t)
        t.start()

    for i in threads:
        i.join()

    #NOW WE MERGE ONE MORE TIME, FOR COMPENSATING THE THREADING PARTITIONING

    #print(result)

    res_left, res_right = result

    final_res = merge(res_left, res_right)

    print(final_res)


start_time = time.time()
exec()
end_time = time.time()

print(end_time - start_time)


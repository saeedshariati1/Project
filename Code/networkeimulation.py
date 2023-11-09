import random

# نرخ ورودی برای هر صف
arrival_rates = [0.5, 1, 2]

# زمان سرویس برای هر صف
service_rates = [1, 2, 3]

# تعداد درخواست های مورد نیاز برای شبیه سازی
num_requests = 10000

# زمان شروع شبیه سازی
start_time = 0

# زمان پایان شبیه سازی
end_time = 1000

# یک صف برای هر صف در شبکه
queues = [[] for _ in range(3)]

# یک لیست برای ذخیره تمام درخواست ها
requests = []

# یک لیست برای ذخیره زمان ورود هر درخواست
arrival_times = []

# یک لیست برای ذخیره زمان شروع سرویس هر درخواست
service_start_times = []

# یک لیست برای ذخیره زمان پایان سرویس هر درخواست
service_end_times = []

# یک لیست برای ذخیره زمان انتظار هر درخواست
wait_times = []

# یک لیست برای ذخیره زمان پاسخ هر درخواست
response_times = []

# یک لیست برای ذخیره نرخ اشغال شبکه
occupancy_rates = []

# یک لیست برای ذخیره تعداد مشتریان در شبکه
number_of_customers = []

# ایجاد درخواست ها
for i in range(num_requests):
    # تولید زمان ورود برای درخواست i
    arrival_time = start_time + random.expovariate(arrival_rates[i])

    # اضافه کردن درخواست i به لیست درخواست ها
    requests.append((i, arrival_time))

    # اضافه کردن زمان ورود درخواست i به لیست زمان ورود
    arrival_times.append(arrival_time)

# مرتب سازی درخواست ها بر اساس زمان ورود
requests.sort(key=lambda x: x[1])

# شبیه سازی شبکه
for request in requests:
    # تعیین صفی که درخواست به آن وارد می شود
    queue_index = 0
    for i in range(1, 3):
        if arrival_times[request[0]] < service_end_times[queues[i-1][-1][0]]:
            queue_index = i
            break

    # اضافه کردن درخواست به صف
    queues[queue_index].append(request)

    # اگر صف خالی باشد، شروع سرویس درخواست
    if len(queues[queue_index]) == 1:
        service_start_times[request[0]] = arrival_times[request[0]]

# محاسبه زمان انتظار و زمان پاسخ هر درخواست
for i in range(num_requests):
    # تعیین صفی که درخواست i در آن قرار دارد
    queue_index = requests[i][0]

    # محاسبه زمان انتظار درخواست i
    wait_times[i] = service_start_times[i] - arrival_times[i]

    # محاسبه زمان پاسخ درخواست i
    response_times[i] = wait_times[i] + service_rates[queue_index]

# محاسبه نرخ اشغال شبکه
for i in range(3):
    occupancy_rates.append(len(queues[i]) / end_time)

# محاسبه تعداد مشتریان در شبکه
for i in range(3):
    number_of_customers.append(sum([1 for request in requests if request[0] == i]))

# چاپ نتایج
print("میانگین زمان انتظار در صف 1:", sum(wait_times) / num_requests)
print("میانگین زمان انتظار در صف 2:", sum(wait_times) / num_requests)
print("میانگین زمان انتظار در صف 3:", sum(wait_times) / num_requests)
print("میانگین زمان پاسخ شبکه:", sum(response_times) / num_requests)
print("نرخ اشغال شبکه:", sum(occupancy_rates))
print("میانگین تعداد مشتریان در شبکه:", sum(number_of_customers) / num_requests)

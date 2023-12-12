import psutil
import time

# Using Psutil

import psutil
import time

# Get the psutil.cpu_times tuple
# https://psutil.readthedocs.io/en/latest/
cpu_times = psutil.cpu_times(percpu=False)

# Variable set with info as required from the tuple
user_time = cpu_times.user
# Same; repeat for the rest
system_time = cpu_times.system
idle_time = cpu_times.idle
priority_user_time = cpu_times.nice
io_wait_time = cpu_times.iowait
irq_time = cpu_times.irq
softirq_time = cpu_times.softirq
guest_time = cpu_times.guest
guest_nice_time = cpu_times.guest_nice

# Print to screen the requirement and the respective variable holding the info
print(f"Time spent by normal processes executing in user mode: {user_time} seconds")
print(f"Time spent by processes executing in kernel mode: {system_time} seconds")
print(f"Time when the system was idle: {idle_time} seconds")
print(f"Time spent by priority processes executing in user mode: {priority_user_time} seconds")
print(f"Time spent waiting for I/O to complete: {io_wait_time} seconds")
print(f"Time spent for servicing hardware interrupts: {irq_time} seconds")
print(f"Time spent for servicing software interrupts: {softirq_time} seconds")
print(f"Time spent by other operating systems running in a virtualized environment: {guest_time} seconds")
print(f"Time spent running a virtual CPU for guest operating systems: {guest_nice_time} seconds")

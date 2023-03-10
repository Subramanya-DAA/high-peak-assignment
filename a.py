def job_selection(n, jobs):
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    earnings = 0
    count = 0
    end_time = 0
    for job in jobs:
        if job[0] >= end_time:
            end_time = job[1]
            earnings += job[2]
            count += 1
    return (n - count, earnings)

n = int(input("enter no of jobs:"))
jobs = []
for i in range(n):
    start_time = int(input("start time:"))
    end_time = int(input("end time:"))
    profit = int(input("profit:"))
    jobs.append((start_time, end_time, profit))

result = job_selection(n, jobs)
print(result[0], result[1])
# to run the code press " F5 "

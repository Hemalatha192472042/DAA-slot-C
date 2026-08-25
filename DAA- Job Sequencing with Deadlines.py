def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * max_deadline

    profit = 0

    for job in jobs:
        name, deadline, value = job

        for i in range(deadline - 1, -1, -1):
            if slots[i] is None:
                slots[i] = name
                profit += value
                break

    print("Job sequence:", slots)
    print("Maximum profit:", profit)


jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

job_sequencing(jobs)

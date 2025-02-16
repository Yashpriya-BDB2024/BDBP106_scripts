def course_info(name, stream="BDB", batch="2024", **kwargs):
    print(f"Name: {name}")
    print(f"Stream: {stream}")
    print(f"Batch: {batch}")
    for key, value in kwargs.items():
        print(f"key: {key}")
        print(f"value: {value}")

def main():
    course_info('Yash Priya Baid')
    course_info('Yash Priya Baid', stream="BTBI", batch="2023")
    course_info('Yash Priya Baid', facilitator='Dr. Nithya Ramakrishnan', type='Python lab')
    course_info('Yash Priya Baid', stream="2020", facilitator='Dr. Nithya Ramakrishnan', location='IBAB')

if __name__ == "__main__":
    main()

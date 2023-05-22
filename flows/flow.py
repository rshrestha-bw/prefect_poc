from prefect import flow, get_run_logger, task, context

@task
def hello_task():
    print("hello")

@flow(name="hello")
def hello_flow():
    hello_task()

if __name__ == "__main__":
   hello_flow()

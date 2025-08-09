from prefect import flow, tags

@flow(log_prints=True)
def olamundo():
	print("Olá Mundo!")
	exit(0)


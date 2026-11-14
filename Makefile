batch:
	# Build and start the aws-emulator
	docker compose build
	docker compose up -d aws-emulator
	
	# Run the s3-client (The emulator is still running in the background)
	docker compose run --rm s3-client

	# Run the dynamodb-client (The emulator is still running in the background)
	docker compose run --rm dynamodb-client
	
	# Run the dynamodb-client (The emulator is still running in the background)
	docker compose run --rm s3-bucket-acl-roundtrip
	
	# Clean up everything at once
	docker compose down -v


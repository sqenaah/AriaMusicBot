utf-8utf-8importasyncio
frompyrogramimportClient

api_id=27638882
api_hash="f745cdd5ddb46cf841d6990048f52935"

asyncdefmain():
    asyncwithClient("assistant",api_id=api_id,api_hash=api_hash)asapp:
        session_string=awaitapp.export_session_string()
print("New session string:")
print(session_string)

asyncio.run(main())

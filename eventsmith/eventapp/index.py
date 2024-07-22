import pusher

pusher_client = pusher.Pusher(
  app_id='1837894',
  key='d6935e17c8a8ab9a4d4d',
  secret='e0edbaafced90c7b641d',
  cluster='ap2',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
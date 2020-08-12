
const beamsClient = new PusherPushNotifications.Client({
  instanceId: '288583d0-a8a6-4d6e-871f-af16b075cd28',
});

beamsClient.start()
  .then(() => beamsClient.addDeviceInterest('hello'))
  .then(() => console.log('Successfully registered and subscribed!'))
  .catch(console.error);
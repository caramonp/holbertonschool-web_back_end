export default function handleResponseFromAPI(promise) {
    return promise.then(() => (
        {
            status: 200,
            body: 'Success',
        }
    )).catch(() => (new Error('The fake API is not working currently')))
    .then(() => (
      console.log('Got a response from the API')
    ));
}

import signUpser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup (firstName, lastName, fileName){
    const promises = [signUpser, uploadPhoto]
    return Promise.allSettled(promises)
    .then((results) => results.forEach((result) => (result)))
}
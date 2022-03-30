import { createUser, uploadPhoto } from "./utils.js";

export default async function asyncUploadUser() {

    function createObject(){
       obj = {
        photo : null,
        user: null
       };
    }
    
    return Promise.all([uploadPhoto(), createUser()]).then(values => ({
            photo: values[0],
            user:  values[1]
    })).catch((e) => ({
        createObject
    }));
}

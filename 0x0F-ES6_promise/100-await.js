import { createUser, uploadPhoto } from './utils';

export default async function asyncUploadUser() {
  function createObject() {
    return {
      photo: null,
      user: null,
    };
  }

  return Promise.all([uploadPhoto(), createUser()]).then((values) => ({
    photo: values[0],
    user: values[1],
  })).catch(() => createObject());
}

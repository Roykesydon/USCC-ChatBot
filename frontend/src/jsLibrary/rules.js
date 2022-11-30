export const rules = {
  required: (value) => !!value || "required",
  arrayRequired: (v) => {
    return v.length > 0 || "required";
  },
  id: (v) => {
    return (
      (v != null && v.length >= 3 && v.length <= 30) ||
      "Must be between 3-30 characters"
    );
  },
  englishAndNumberOnly: (v) => {
    const pattern = /[A-Za-z0-9]*$/;
    return (
      (v != null && pattern.test(v)) || "english & numeric characters only"
    );
  },
  emailFormat: (value) => {
    const pattern =
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return (value != null && pattern.test(value)) || "email format error";
  },
  emailLength: (v) => {
    return (
      (v != null && v.length >= 3 && v.length <= 50) ||
      "Must be between 3-50 characters"
    );
  },
  password: (v) => {
    return (
      (v != null && v.length >= 3 && v.length <= 30) ||
      "Must be between 6-30 characters"
    );
  },
};

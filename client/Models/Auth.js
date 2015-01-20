var request = require('browser-request');

function Auth(username, password) {
  this.username = username;
  this.password = password;
}

Auth.prototype.login = function() {
  request.post({
    url: '/auth',
    json: {
      username: this.username,
      password: this.password
    }
  }, function(error, response) {
    if (error) {
      throw error;
    }
    if (result.ok) {
      console.log(result.body);
    }
  });
};
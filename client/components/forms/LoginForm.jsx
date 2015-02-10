var React = require('react')
var TextField = require('./TextField.jsx')
var PasswordField = require('./PasswordField.jsx')
var FormSubmit = require('./FormSubmit.jsx')

message = ''

function usernameValidate(username) {
  var re = /^([a-zA-Z0-9_])*?$/g
  if (username.length < 1) {
    message = 'Username field is empty'
    return false
  }
  if (!re.text(username)) {
    message = 'Username must only contain letters, numbers, and underscores'
    return false
  }
  return true
}

function getErrorMessage() {
  return message
}

var LoginForm = React.createClass({
  isValid: function() {
    return (this.refs['usernameField'].isValid() &&
            this.refs['passwordField'].isValid())
  },
  render: function() {
    return (
      <form id="loginForm">
        <TextField
          name='username'
          label='Username'
          validate={usernameValidate}
          getErrorMessage={getErrorMessage}
          ref='usernameField' />
        <PasswordField ref='passwordField' />
        <FormSubmit validate={this.isValid} />
      </form>
    )
  }

})

module.exports = LoginForm


var React = require('react')
var cx = React.addons.classSet


var PasswordField = React.createClass({
  getCurrentState: function() {
    return {
      password: $("#password").val(),
      confirm: $("#confirm").val()
    }
  },
  getInitialState: function() {
    return {
      password: "",
      confirm: ""
    }
  },
  isValid: function() {
    return this.isPasswordValid() && this.isConfirmValid()
  },
  isValidValue: function(value) {
    return (value.length >= 6)
  },
  isPasswordValid: function() {
    return this.isValidValue(this.state.password)
  },
  isConfirmValid: function() {
    return this.isValidValue(this.state.confirm) &&
           this.state.confirm == this.state.password
  },
  render: function() {
    var passwordClasses = cx({
      'form-control': true,
      'has-error': this.isPasswordValid(),
      'has-success': !this.isPasswordValid()
    });
    var confirmClasses = cx({
      'form-control': true,
      'has-error': this.isConfirmValid(),
      'has-success': !this.isConfirmValid()
    });
    return (
      <div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            className={passwordClasses}
            id="password"
            type="password"
            name="password" />
        </div>
        <div className="form-group">
          <label htmlFor="confirm">Confirm Passowrd</label>
          <input
            className={confirmClasses}
            id="confirm"
            type="password"
            name="confirm" />
        </div>
      </div>
    )
  }
})

module.exports = PasswordField
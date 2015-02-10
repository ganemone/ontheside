var React = require('react')

var FormSubmit = React.createClass({
  isValid: function() {
    if (this.hasValidator()) {
      return this.props.validator()
    }
    return true
  },
  hasValidator: function() {
    return (typeof this.props.validator === 'function')
  },
  render: function() {
    var cx = React.addons.classSet
    var classes = cx({
      'btn': true,
      'btn-default': true,
      'btn-disabled': !this.isValid()
    });
    return (
      <button type="submit" className={classes}>Submit</button>
    )
  }
})

module.exports = FormSubmit
var React = require('react');

var TextField = React.createClass({

  getCurrentState: function() {
    var state = {}
    state[this.props.name] = $("#" + this.props.name).val()
    return state
  },
  getInitialState: function() {
    var state = {}
    state[this.props.name] = ''
    return state
  },
  getValue: function() {
    return this.state[this.props.name]
  },
  isValid: function() {
    if (this.hasValidator()) {
      return this.props.validate(this.getValue())
    }
    return true
  },
  hasValidator: function() {
    return (typeof this.props.validate === 'function')
  },
  render: function() {
    var cx = React.addons.classSet
    var classes = cx({
      'form-control': true,
      'has-error': (!this.isValid()),
      'has-success': (this.hasValidator() && this.isValid())
    });
    return (
      <div className="form-group">
        <label htmlFor={this.props.name}>{this.props.label}</label>
        <input
          className={classes}
          type='text'
          name={this.props.name}
          id={this.props.name} />
      </div>
    );
  }
});

module.exports = TextField;
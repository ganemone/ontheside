/** @jsx React.DOM */
var React = require('react/addons');
var ComponentTypes = require('../constants/ComponentTypes');
var cx = React.addons.classSet;
var NavBarItem = React.createClass({
  displayName: 'NavBarItem',
  getInitialState: function() {
    return {
      isActive: this.props.isInitiallyActive
    };
  },
  getDefaultProps: function() {
    return {
      data: {
        action: '#'
      }
    };
  },
  render: function() {
    var classes = cx({
      'active': this.state.isActive
    });
    return (
      <li key={this.props.id} className={classes}>
        <a href={this.props.data.action}>{this.props.data.text}</a>
      </li>
    );
  }
});

module.exports = NavBarItem;
/** @jsx React.DOM */
var React = require('react/addons');
var ComponentTypes = require('../constants/ComponentTypes');
var Router = require('react-router');
var cx = React.addons.classSet;
var NavBarItem = React.createClass({
  displayName: 'NavBarItem',
  mixins: [Router.State],
  getAction: function() {
    return '/#' + this.props.data.action
  },
  render: function() {
    var classes = cx({
      'active': this.props.isActive
    });
    return (
      <li key={this.props.id} className={classes}>
        <a href={this.getAction()}>{this.props.data.text}</a>
      </li>
    );
  }
});

module.exports = NavBarItem;